# Resumen de resultados — Regresión RB

## Muestra y EDA

- 360 observaciones semanales entre 2010 y 2016; 10 variables; 0 valores faltantes.
- Ventas semanales: media 56,470.02; desviación estándar 28,141.14; mínimo 17,924; máximo 214,707.80.
- Correlaciones de Pearson entre ventas y promociones: Display 0.815; Lote/Pack 0.602; Folleto 0.306; Display + Folleto 0.281; Cupón 0.220; Cantidad Extra 0.010.
- Semanas con cero acciones: Folleto 40; Display + Folleto 104; Lote/Pack 303; Cantidad Extra 351; Cupón 345.
- El volumen promedio anual baja en 2012 (36,326.27) respecto a 2011 (43,205.08) y crece posteriormente hasta 98,662.66 en 2016.

## Especificación estimada

- Variable dependiente: `TotalvolmeRB`.
- Predictores incluidos: `DispRB`, `FollRB`, `DisfoRB` y `LoteRB`.
- `CanexRB` y `CupoRB` se excluyen de la especificación principal por presentar solo 9 y 15 semanas con acciones positivas, respectivamente.
- `TotalPromosRB` no se combina con las seis categorías desagregadas porque el diccionario la define como su suma.

## Ajuste OLS

- R² = 0.7139; R² ajustado = 0.7107.
- F global OLS = 221.44; p = 4.39e-95.
- RMSE dentro de muestra = 15,031.76; MAE = 11,229.29.

| Variable | Coeficiente OLS | Error estándar OLS | p-valor OLS | Error estándar HAC (4 rezagos) | p-valor HAC |
|---|---:|---:|---:|---:|---:|
| Constante | 31,473.02 | 1,307.06 | <0.001 | 1,974.85 | <0.001 |
| DispRB | 154.80 | 8.25 | <0.001 | 14.21 | <0.001 |
| FollRB | 12.10 | 27.40 | 0.659 | 40.77 | 0.767 |
| DisfoRB | 358.20 | 87.55 | <0.001 | 134.45 | 0.0081 |
| LoteRB | 614.50 | 111.64 | <0.001 | 250.05 | 0.0145 |

## Contraste robusto de hipótesis

Se utilizó covarianza HAC/Newey–West con cuatro rezagos:

- **H1 (efecto conjunto de los cuatro predictores incluidos):** F robusta = 44.89; p = 1.69e-30. Se rechaza la hipótesis nula de que los cuatro coeficientes sean simultáneamente cero.
- **H2 (igualdad de las cuatro pendientes):** F robusta = 4.18; p = 0.0063. Se rechaza la igualdad de los coeficientes de Display, Folleto, Display + Folleto y Lote/Pack al 5%.

Estas pruebas se aplican solo a los cuatro predictores de la especificación, no a CanexRB o CupoRB, que fueron excluidos. La comparación de pendientes representa asociaciones por unidad de conteo y no considera costos ni rentabilidad de cada promoción.

## Diagnósticos y validación temporal

- Durbin–Watson = 0.507; Breusch–Godfrey p = 1.15e-45: fuerte evidencia de autocorrelación positiva.
- Breusch–Pagan p = 8.37e-06: evidencia de heterocedasticidad.
- Jarque–Bera p = 8.27e-263: residuos no normales.
- VIF de los predictores entre 1.52 y 1.69: no se observa multicolinealidad severa.
- Validación temporal: entrenamiento 2010–2015; prueba 2016 (48 observaciones): R² = 0.3601, RMSE = 22,600.31 y MAE = 18,273.86.

## Interpretación

Display, Display + Folleto y Lote/Pack conservan una asociación positiva estadísticamente significativa con ventas al utilizar inferencia HAC. Folleto no muestra evidencia de asociación incremental al controlar por los demás formatos. La dependencia temporal, heterocedasticidad, variables omitidas y caída del desempeño en 2016 impiden interpretar los coeficientes como efectos causales o usar el modelo como regla automática de inversión.

**Recomendación:** probar las promociones en diseños controlados por tiendas y semanas comparables, capturar costos/márgenes/precios/inventario, y desarrollar un modelo temporal con variables de estacionalidad, rezagos y validación rolling-origin.
