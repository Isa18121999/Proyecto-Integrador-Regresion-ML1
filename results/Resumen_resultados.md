# Resumen de resultados — Regresión RB

## Muestra y especificación

- 360 observaciones semanales entre 2010 y 2016; 0 valores faltantes.
- Variable dependiente: `TotalvolmeRB`.
- Predictores incluidos: `DispRB`, `FollRB`, `DisfoRB` y `LoteRB`.
- Se excluyeron `CanexRB` y `CupoRB` por su extrema concentración de ceros.
- `TotalPromosRB` no se combina con las seis categorías desagregadas porque el diccionario la define como su suma.

## Ajuste OLS

- R² = 0.7139; R² ajustado = 0.7107.
- F global OLS = 221.44; p = 4.39e-95.
- RMSE dentro de muestra = 15,031.76; MAE = 11,229.29.

| Variable | Coeficiente OLS | Error estándar HAC (4 rezagos) | p-valor HAC |
|---|---:|---:|---:|
| Constante | 31,473.02 | 1,974.85 | <0.001 |
| DispRB | 154.80 | 14.21 | <0.001 |
| FollRB | 12.10 | 40.77 | 0.767 |
| DisfoRB | 358.20 | 134.45 | 0.008 |
| LoteRB | 614.50 | 250.05 | 0.014 |

## Contraste robusto de hipótesis

Se utilizó covarianza HAC/Newey–West con cuatro rezagos:

- **H1 (efecto conjunto de las promociones incluidas):** F robusta = 44.89; p = 1.69e-30. Se rechaza que los cuatro coeficientes incluidos sean simultáneamente cero.
- **H2 (igualdad de las cuatro pendientes):** F robusta = 4.18; p = 0.0063. Se rechaza la igualdad de los coeficientes de Display, Folleto, Display + Folleto y Lote/Pack al 5%.

Estas pruebas se aplican solo a los cuatro predictores de la especificación, no a CanexRB o CupoRB, que fueron excluidos. La comparación de pendientes representa asociaciones por unidad de conteo y no considera costos ni rentabilidad de cada promoción.

## Diagnósticos y validación temporal

- Durbin–Watson = 0.507; Breusch–Godfrey p = 1.15e-45: fuerte evidencia de autocorrelación positiva.
- Breusch–Pagan p = 8.37e-06: evidencia de heterocedasticidad.
- Jarque–Bera p = 8.27e-263: residuos no normales.
- VIF de los predictores entre 1.52 y 1.69: no se observa multicolinealidad severa.
- Validación temporal: entrenamiento 2010–2015; prueba 2016 (48 observaciones): R² = 0.3601, RMSE = 22,600.31 y MAE = 18,273.86.

## Interpretación

Los resultados muestran asociaciones positivas robustas para Display, Display + Folleto y Lote/Pack en la especificación estimada. Folleto no presenta evidencia de asociación incremental una vez controlados los otros predictores. La dependencia temporal, heterocedasticidad, variables omitidas y caída del desempeño en 2016 impiden interpretar los coeficientes como efectos causales o usar el modelo como regla automática de inversión.

**Recomendación:** probar las promociones en diseños controlados por tiendas y semanas comparables, capturar costos/márgenes/precios/inventario, y desarrollar un modelo temporal con variables de estacionalidad, rezagos y validación rolling-origin.
