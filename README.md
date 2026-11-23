# Proyecto Integrador – Regresión de ventas de bebidas energéticas RB

Proyecto de Análisis Multivariado I de la Universidad ESAN. Se desarrolla el caso RB de bebidas energéticas mediante regresión lineal múltiple.

## Objetivo de negocio
Analizar la relación entre los distintos formatos de promoción comercial y el volumen semanal de ventas de RB en supermercados e hipermercados para aportar evidencia a la planificación de marketing.

## Estructura del repositorio
- `data/BD_REGRESION.csv`: base original convertida desde Excel (360 semanas, 2010–2016).
- `data/DICCIONARIO_VARIABLES_RB.md`: descripción de variables y criterio de selección.
- `docs/Informe_Regresion_RB.md`: informe académico con los siete apartados de la guía.
- `src/analisis_regresion.py`: análisis reproducible en Python.
- `results/Resumen_resultados.md`: resumen del EDA, modelo, pruebas HAC y diagnósticos.
- `results/coeficientes_modelo.csv`, `results/diagnosticos.csv`: resultados numéricos del modelo.
- `results/estadisticos_descriptivos.csv`, `results/ventas_por_anio.csv`: EDA tabular.
- `results/validacion_temporal_2016.csv`: evaluación temporal con 2016 como periodo de prueba.
- `requirements.txt`: dependencias necesarias.
- `figures/`: gráficos generados al ejecutar el script.

## Modelo principal
Variable dependiente: `TotalvolmeRB`. Predictores: `DispRB`, `FollRB`, `DisfoRB` y `LoteRB`. R² = 0.7139 y R² ajustado = 0.7107.

No se incorpora `TotalPromosRB` junto con las variables promocionales desagregadas, porque el diccionario la define como suma de las seis categorías. `CanexRB` y `CupoRB` se excluyen de la regresión principal por su escasez extrema: solo aparecen en 9 y 15 semanas, respectivamente.

## Resultados y cautelas
Se complementó la inferencia con errores estándar HAC/Newey–West (4 rezagos). Las pruebas robustas apoyan un efecto conjunto de los cuatro predictores incluidos y rechazan la igualdad de sus pendientes. Display, Display + Folleto y Lote/Pack mantienen significancia individual al 5%; Folleto no. Los diagnósticos muestran autocorrelación y heterocedasticidad, y la validación temporal en 2016 arroja R² = 0.360. Los coeficientes son asociaciones, no efectos causales ni medidas de rentabilidad.

## Ejecución local
Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar desde la raíz:

```bash
python src/analisis_regresion.py
```

El script guarda coeficientes, diagnósticos, descriptivos, ventas por año, resumen OLS, residuos, validación temporal y las figuras (incluida la ACF residual) en `results/` y `figures/`.

## Material de origen
El caso y la estructura académica se basan en la presentación del Proyecto Integrador de Análisis Multivariado I. El informe desarrolla los siete apartados solicitados y explicita los alcances y limitaciones del modelo.
