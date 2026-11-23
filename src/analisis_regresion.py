"""Proyecto Integrador RB - regresión lineal múltiple.
Ejecutar desde la raíz del repositorio: python src/analisis_regresion.py
Lee data/BD_REGRESION.csv y genera archivos en results/ y figures/.
"""
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.diagnostic import het_breuschpagan, acorr_breusch_godfrey
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "BD_REGRESION.csv"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)
TARGET = "TotalvolmeRB"
FEATURES = ["DispRB", "FollRB", "DisfoRB", "LoteRB"]

def main():
    if not DATA.exists():
        raise FileNotFoundError(f"No se encontró el dataset: {DATA}")
    df = pd.read_csv(DATA)
    required = ["año", "semana", TARGET, *FEATURES]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")
    if df[required].isna().any().any():
        warnings.warn("Se detectaron valores faltantes en variables del análisis.")

    X = sm.add_constant(df[FEATURES])
    y = df[TARGET]
    model = sm.OLS(y, X).fit()
    # Errores estándar HAC/Newey-West para complementar inferencia OLS.
    hac = model.get_robustcov_results(cov_type="HAC", maxlags=4)
    # Contrastes conjuntos robustos para H1 y H2, sobre los cuatro predictores incluidos.
    h1_robust = hac.f_test("DispRB=0, FollRB=0, DisfoRB=0, LoteRB=0")
    h2_robust = hac.f_test("DispRB=FollRB, DispRB=DisfoRB, DispRB=LoteRB")

    output = df.copy()
    output["Ventas_estimadas"] = model.predict(X)
    output["Residuo"] = model.resid
    output.to_csv(RESULTS / "ventas_estimadas_y_residuos.csv", index=False, encoding="utf-8-sig")

    coef = pd.DataFrame({
        "variable": model.params.index,
        "coeficiente_OLS": model.params.values,
        "error_estandar_OLS": model.bse.values,
        "pvalor_OLS": model.pvalues.values,
        "error_estandar_HAC": hac.bse,
        "pvalor_HAC": hac.pvalues,
    })
    coef.to_csv(RESULTS / "coeficientes_modelo.csv", index=False, encoding="utf-8-sig")
    (RESULTS / "resumen_OLS.txt").write_text(model.summary().as_text(), encoding="utf-8")

    bp = het_breuschpagan(model.resid, model.model.exog)
    bg = acorr_breusch_godfrey(model, nlags=1)
    jb = jarque_bera(model.resid)
    vif = {c: variance_inflation_factor(X.values, i + 1) for i, c in enumerate(FEATURES)}
    diagnostics = [
        ("n_observaciones", len(df)), ("R2", model.rsquared),
        ("R2_ajustado", model.rsquared_adj), ("F_global", model.fvalue),
        ("pvalor_F", model.f_pvalue),
        ("RMSE_in_sample", np.sqrt(mean_squared_error(y, model.predict(X)))),
        ("MAE_in_sample", mean_absolute_error(y, model.predict(X))),
        ("Durbin_Watson", durbin_watson(model.resid)),
        ("Breusch_Pagan_LM", bp[0]), ("Breusch_Pagan_p", bp[1]),
        ("Breusch_Godfrey_LM", bg[0]), ("Breusch_Godfrey_p", bg[1]),
        ("Jarque_Bera", jb[0]), ("Jarque_Bera_p", jb[1]),
        ("H1_F_HAC_4lags", float(h1_robust.fvalue)),
        ("H1_p_HAC_4lags", float(h1_robust.pvalue)),
        ("H2_equal_slopes_F_HAC_4lags", float(h2_robust.fvalue)),
        ("H2_equal_slopes_p_HAC_4lags", float(h2_robust.pvalue)),
    ] + [(f"VIF_{k}", v) for k, v in vif.items()]
    pd.DataFrame(diagnostics, columns=["metrica", "valor"]).to_csv(RESULTS / "diagnosticos.csv", index=False)

    # Estadística descriptiva y frecuencia de ceros por variable.
    desc = df[[TARGET, *FEATURES, "CanexRB", "CupoRB"]].describe().T
    desc["ceros"] = (df[[TARGET, *FEATURES, "CanexRB", "CupoRB"]] == 0).sum()
    desc.to_csv(RESULTS / "estadisticos_descriptivos.csv", encoding="utf-8-sig")
    df.groupby("año")[TARGET].agg(["count", "mean", "min", "max"]).to_csv(
        RESULTS / "ventas_por_anio.csv", encoding="utf-8-sig"
    )

    # Validación temporal: entrenar 2010-2015 y evaluar el año 2016.
    train, test = df["año"] < 2016, df["año"] == 2016
    if train.any() and test.any():
        lr = LinearRegression().fit(df.loc[train, FEATURES], y[train])
        pred = lr.predict(df.loc[test, FEATURES])
        pd.DataFrame([{
            "periodo_test": "2016", "n_test": int(test.sum()),
            "R2": r2_score(y[test], pred),
            "RMSE": np.sqrt(mean_squared_error(y[test], pred)),
            "MAE": mean_absolute_error(y[test], pred),
        }]).to_csv(RESULTS / "validacion_temporal_2016.csv", index=False)

    # EDA y diagnóstico visual.
    plt.figure(figsize=(9, 5))
    df.groupby("año")[TARGET].mean().plot(marker="o")
    plt.title("Promedio anual de ventas RB"); plt.xlabel("Año")
    plt.ylabel("Volumen semanal promedio"); plt.tight_layout()
    plt.savefig(FIGURES / "ventas_anuales.png", dpi=160); plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["DispRB"], y, alpha=.65)
    plt.title("Display y volumen semanal de ventas")
    plt.xlabel("Acciones Display"); plt.ylabel("Volumen de ventas"); plt.tight_layout()
    plt.savefig(FIGURES / "display_ventas.png", dpi=160); plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(model.fittedvalues, model.resid, alpha=.65)
    plt.axhline(0, linestyle="--")
    plt.title("Residuos frente a valores ajustados")
    plt.xlabel("Valores ajustados"); plt.ylabel("Residuos"); plt.tight_layout()
    plt.savefig(FIGURES / "residuos.png", dpi=160); plt.close()

    # Función de autocorrelación residual para evaluar dependencia temporal.
    fig, ax = plt.subplots(figsize=(9, 5))
    plot_acf(model.resid, lags=30, ax=ax)
    ax.set_title("Autocorrelación de residuos (30 rezagos)")
    ax.set_xlabel("Rezago (semanas)")
    fig.tight_layout()
    fig.savefig(FIGURES / "acf_residuos.png", dpi=160)
    plt.close(fig)

    corr = df[[TARGET, *FEATURES]].corr()
    plt.figure(figsize=(7, 6))
    plt.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
    plt.colorbar(label="Correlación de Pearson")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=35, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.title("Correlaciones entre ventas y promociones"); plt.tight_layout()
    plt.savefig(FIGURES / "correlaciones.png", dpi=160); plt.close()

    print(model.summary())
    print("\nInferencia robusta HAC/Newey-West (4 rezagos):")
    print(pd.DataFrame({"coeficiente": model.params, "SE_HAC": hac.bse, "p_HAC": hac.pvalues}))
    print("\nResultados en results/; gráficos en figures/.")

if __name__ == "__main__":
    main()
