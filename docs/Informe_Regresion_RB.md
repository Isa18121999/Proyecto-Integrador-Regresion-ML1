# Universidad ESAN
## Ingeniería de Tecnología de Información y Sistemas
### Análisis Multivariado I — Proyecto Integrador

# Modelo de regresión para explicar el volumen de ventas de bebidas energéticas RB

**Docente:** Mg. Omar A. Chincaro Del C.  
**Integrantes:** [Completar nombres]  
**Fecha:** 23 de noviembre de 2026

## Resumen ejecutivo

Este proyecto analiza el volumen semanal de ventas de bebidas energéticas RB en supermercados e hipermercados a partir de 360 observaciones de 2010–2016. Se estima una regresión lineal múltiple con cuatro tipos de acciones promocionales: Display, Folleto, Display + Folleto y Lote/Pack. El modelo obtiene R² = 0.714 y R² ajustado = 0.711. Display, Display + Folleto y Lote/Pack presentan coeficientes positivos y estadísticamente significativos en la especificación estimada; Folleto no es significativo al controlar por los demás tipos. Los diagnósticos detectan autocorrelación, heterocedasticidad y falta de normalidad residual, por lo que los resultados se interpretan como asociaciones y no como efectos causales. Se recomienda un modelo temporal con errores robustos y validación fuera de muestra antes de tomar decisiones de inversión.

## 1. Planteamiento del objetivo de negocios

La marca RB busca evaluar el rendimiento de las acciones promocionales implementadas en los canales supermercado e hipermercado. El negocio necesita comprender qué formatos promocionales se relacionan con un mayor volumen semanal de ventas para orientar la asignación del presupuesto comercial, mejorar la ejecución en el punto de venta y reducir la dependencia de decisiones basadas únicamente en intuición.

**Objetivo de negocio:** optimizar la planificación de las promociones de RB, identificando los tipos de acción asociados con mayores volúmenes de venta semanal y generando criterios para distribuir eficientemente los recursos comerciales.

## 2. Planteamiento de objetivos analíticos

1. Describir la distribución y evolución del volumen semanal de ventas de RB entre 2010 y 2016.
2. Explorar la relación entre las ventas y los seis tipos de acciones promocionales disponibles.
3. Estimar un modelo de regresión lineal múltiple que cuantifique la asociación de cada formato promocional con el volumen semanal de ventas.
4. Contrastar si las promociones influyen conjuntamente en las ventas y si todos los tipos presentan la misma asociación con la variable dependiente.
5. Evaluar el ajuste y los supuestos del modelo, identificando limitaciones para su uso predictivo y proponiendo mejoras.

## 3. Planteamiento de hipótesis

Se retoman las hipótesis del caso de bebidas energéticas de la presentación del curso (página 10):

**H1. Las promociones influyen en las ventas.**

- H0₁: βDisp = βFoll = βDisfo = βLote = βCanex = βCupo = 0.
- H1₁: al menos uno de los coeficientes de promoción es distinto de cero.

**H2. Todos los tipos de promoción tienen el mismo efecto sobre las ventas.**

- H0₂: los coeficientes asociados a los tipos de promoción son iguales.
- H1₂: al menos dos coeficientes difieren.

**Nota metodológica:** la base no contiene asignación aleatoria ni controles completos de precio, distribución, estacionalidad comercial o inversión publicitaria. Por ello, el análisis contrasta asociaciones estadísticas, no causalidad. Además, como los tipos de promoción tienen escalas y frecuencias muy diferentes, la comparación de coeficientes debe considerar unidades, intervalos de confianza y pruebas conjuntas; no basta con comparar sus valores numéricos.

## 4. Análisis exploratorio de datos (EDA)

La base `data/BD_REGRESION.csv` contiene 360 registros y 10 variables. Cada observación representa una semana, con identificadores de año y semana, ventas totales y conteos de promociones. El diccionario identifica `TotalvolmeRB` como variable dependiente, `TotalPromosRB` como suma de las seis acciones promocionales, y las seis variables desagregadas como predictores potenciales.

La media del volumen semanal aumenta de forma general a lo largo del periodo, con una caída relativa en 2012 y crecimiento marcado a partir de 2013. Este patrón temporal sugiere que las ventas también pueden estar asociadas a tendencias de mercado y otras variables no incluidas en el archivo.

La correlación de Pearson entre ventas y Display es 0.815; entre ventas y Lote/Pack es 0.602; Folleto registra 0.306, y Display + Folleto 0.281. Estos valores describen asociación lineal bivariada, no efecto causal.

La variable CanexRB presenta 351 semanas con cero acciones, mientras CupoRB presenta 345 semanas con cero y LoteRB 303 semanas con cero. Esta fuerte concentración en cero limita la precisión con que se pueden estimar sus asociaciones y aconseja estudiar estos formatos con mayor volumen de observaciones.

### Resumen descriptivo

| Característica | Resultado |
|---|---:|
| Periodo | 2010–2016 |
| Observaciones | 360 |
| Valores faltantes | 0 |
| Ventas semanales: media | 56,470.02 |
| Ventas semanales: desviación estándar | 28,141.14 |
| Ventas: mínimo – máximo | 17,924.00 – 214,707.80 |
| Promociones totales: media | 174.72 |
| Display: media por semana | 128.91 |
| Folleto: media por semana | 34.82 |

## 5. Solución analítica: modelo de regresión

### 5.1 Definición de variables

Se estimó una especificación con cuatro predictores. CanexRB y CupoRB se excluyeron de la especificación final por su extrema escasez (351 y 345 ceros, respectivamente), pero deben considerarse en una ampliación de datos. FollRB se mantuvo para contrastar su aporte incremental. `TotalPromosRB` no se incorporó junto con los tipos desagregados, porque es la suma de las seis variables y produciría redundancia lineal según el diccionario del proyecto.

| Rol | Variable | Descripción |
|---|---|---|
| Dependiente (Y) | TotalvolmeRB | Volumen total semanal de ventas RB en supermercados e hipermercados |
| Predictora | DispRB | Acciones de exhibición / Display sin folleto ni descuento |
| Predictora | FollRB | Acciones de folleto o publicidad en catálogo del detallista |
| Predictora | DisfoRB | Acciones combinadas de Display + Folleto |
| Predictora | LoteRB | Acciones de lote o pack promocional |

### 5.2 Especificación matemática

Modelo de regresión lineal múltiple:

`Ventas = β₀ + β₁(Display) + β₂(Folleto) + β₃(Display+Folleto) + β₄(Lote/Pack) + ε`

Estimación por mínimos cuadrados ordinarios:

`Ŷ = 31,473.02 + 154.80·DispRB + 12.10·FollRB + 358.20·DisfoRB + 614.50·LoteRB`

### 5.3 Resultados del modelo

El modelo explica 71.39% de la variación observada en ventas (R² = 0.714; R² ajustado = 0.711). La prueba F global es 221.44 con p-valor 4.39e-95, por lo que se rechaza la hipótesis nula de que todos los coeficientes promocionales sean simultáneamente cero en esta especificación.

Manteniendo constantes los demás predictores, una acción adicional de Display se asocia con 154.80 unidades adicionales de ventas semanales (p < 0.001); una acción de Display + Folleto, con 358.20 (p < 0.001); y una acción de Lote/Pack, con 614.50 (p < 0.001). El coeficiente de Folleto es 12.10, pero no es estadísticamente significativo (p = 0.659) al controlar por los otros formatos.

Estos coeficientes son cambios asociados por unidad de conteo de cada promoción; no deben compararse sin considerar la frecuencia y escala de cada variable. En particular, una acción combinada puede requerir mayor inversión que una exhibición simple, información que no está incluida en la base.

| Variable | Coeficiente | Error estándar | p-valor | IC 95% |
|---|---:|---:|---:|---|
| const | 31,473.022 | 1,307.061 | 1.235e-76 | [28,902.47, 34,043.58] |
| DispRB | 154.805 | 8.254 | 4.946e-55 | [138.57, 171.04] |
| FollRB | 12.104 | 27.397 | 0.6589 | [-41.78, 65.98] |
| DisfoRB | 358.203 | 87.554 | 5.315e-05 | [186.01, 530.39] |
| LoteRB | 614.495 | 111.641 | 7.119e-08 | [394.93, 834.06] |

### 5.4 Contraste de hipótesis

**H1:** respaldada para el modelo estimado. La prueba F global resulta significativa (p < 0.001), indicando que, en conjunto, los predictores seleccionados aportan información estadística para explicar las ventas.

**H2:** no queda resuelta de forma concluyente con una comparación informal de coeficientes. El hecho de que algunos p-valores sean significativos y otros no no demuestra que los efectos sean distintos entre sí. Para contrastarla correctamente se requiere una prueba de restricciones lineales entre coeficientes, idealmente con errores estándar robustos que contemplen la dependencia temporal. Dado que el diagnóstico detecta autocorrelación y heterocedasticidad, se recomienda reportar H2 como pendiente de confirmación robusta, no como aceptada o rechazada.

### 5.5 Diagnóstico y limitaciones

El error cuadrático medio de raíz (RMSE) dentro de la muestra es 15,032 unidades de venta y el error absoluto medio (MAE) es 11,229. Al entrenar con 2010–2015 y evaluar en 2016, el R² de prueba es 0.360, con RMSE de aproximadamente 22,600 unidades. El resultado advierte que el poder predictivo se reduce cuando se respeta el orden temporal.

| Diagnóstico | Resultado | Interpretación |
|---|---|---|
| Multicolinealidad | VIF entre 1.52 y 1.69 | No se observa multicolinealidad severa entre los cuatro predictores |
| Autocorrelación | Durbin–Watson = 0.507 | Indicio fuerte de autocorrelación positiva; confirmada por Breusch–Godfrey p < 0.001 |
| Heterocedasticidad | Breusch–Pagan p = 8.4e-06 | Se rechaza homocedasticidad; errores estándar OLS convencionales pueden ser inadecuados |
| Normalidad residual | Jarque–Bera p = 8.3e-263 | Los residuos se apartan de la normalidad |
| Validación temporal | Año 2016: R² = 0.360 | El rendimiento fuera de muestra es menor que el ajuste dentro de muestra |

**Limitaciones:** no se dispone de precio, descuentos monetarios, inversión en medios, distribución numérica, inventarios, competidores, demanda por tienda ni información de causalidad. La autocorrelación también sugiere que la tendencia y la estacionalidad semanal no están suficientemente modeladas. Se recomienda estimar una regresión dinámica o modelo de series temporales, incorporar tendencia, estacionalidad y rezagos de ventas/promoción, y calcular errores estándar HAC/Newey–West o modelos con estructura AR.

## 6. Planteamiento de estrategias a partir de los datos y la solución analítica

1. Priorizar pruebas controladas de Display, dado que presenta la asociación positiva más consistente y la mayor correlación bivariada con ventas. Desplegar pilotos por tienda y semanas comparables, midiendo ventas incrementales y costo por unidad incremental.
2. Evaluar acciones combinadas Display + Folleto y Lote/Pack como alternativas complementarias, calculando margen incremental y retorno promocional antes de escalar; los coeficientes estimados no incorporan costos ni rentabilidad.
3. No retirar Folleto únicamente por su p-valor no significativo en esta especificación. Revisar solapamiento con Display, diseño de la promoción, segmentación de tiendas y potencia estadística del análisis.
4. Recolectar más observaciones para Cantidad Extra y Cupón, ya que aparecen en muy pocas semanas. Hasta entonces, no extraer conclusiones sobre su efectividad.
5. Implementar un tablero semanal con ventas, tipo de promoción, tienda/canal, precio, margen, inventario y distribución. Monitorear métricas como ventas incrementales, margen incremental, ROI promocional y repetición de compra.
6. Antes de fijar presupuestos definitivos, utilizar una regresión temporal con variables de control y validación rolling-origin; comparar el pronóstico con un modelo base sin promociones.

## 7. Conclusiones y recomendaciones

1. La base incluye 360 semanas de información entre 2010 y 2016, sin valores faltantes en las variables disponibles.
2. El modelo lineal múltiple seleccionado presenta un R² de 0.714 y una prueba F global significativa, lo que indica que los tipos de promoción considerados aportan información conjunta para explicar la variación semanal de ventas.
3. Display, Display + Folleto y Lote/Pack muestran asociaciones positivas y estadísticamente significativas en la especificación estimada. Folleto no presenta evidencia de asociación incremental una vez controlados los demás formatos.
4. Los resultados no deben interpretarse como efectos causales ni convertirse directamente en previsiones de rentabilidad, porque no se observan costos, márgenes, precios ni asignación experimental.
5. La autocorrelación, heterocedasticidad y falta de normalidad residual limitan la inferencia OLS convencional. Se necesita un modelo temporal con errores robustos y evaluación fuera de muestra.
6. La recomendación principal es priorizar experimentos medibles para Display y acciones combinadas/pack, ampliar la captura de información comercial y utilizar el análisis como apoyo a decisiones, no como regla automática de inversión.

## Anexo A. Diccionario de variables utilizado

| Variable | Tipo | Descripción | Rol |
|---|---|---|---|
| año | Entero | Año calendario de la observación | Identificador temporal |
| semana | Entero | Número de semana ISO dentro del año | Identificador temporal |
| TotalvolmeRB | Continua | Volumen total de ventas de RB en la semana, en el panel Supermercado/Hipermercado | Variable dependiente (Y) |
| TotalPromosRB | Entero | Número total de acciones promocionales realizadas en la semana (suma de las 6 variables de tipo de promoción) | Predictor agregado; no usar junto con las 6 desagregadas |
| DispRB | Entero | Nº de acciones de Exhibición / Display (colocación destacada del producto, sin folleto ni descuento) | Predictor (X) |
| FollRB | Entero | Nº de acciones de Folleto (publicidad en encarte/catálogo del detallista) | Predictor (X) |
| DisfoRB | Entero | Nº de acciones combinadas de Display + Folleto | Predictor (X) |
| CanexRB | Entero | Nº de acciones de Cantidad Extra (más producto por el mismo precio) | Predictor (X) |
| LoteRB | Entero | Nº de acciones de Lote / Pack promocional | Predictor (X) |
| CupoRB | Entero | Nº de acciones de Cupón (descuento vía cupón redimible) | Predictor (X) |

## Anexo B. Reproducibilidad

Los cálculos se realizaron a partir de `data/BD_REGRESION.csv`. El script `src/analisis_regresion.py` reproduce la especificación OLS, genera los diagnósticos de residuos, estima una inferencia complementaria HAC/Newey–West y realiza una validación temporal con 2010–2015 como entrenamiento y 2016 como prueba.

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

Ejecución desde la raíz del repositorio:

```bash
python src/analisis_regresion.py
```

**Fuente principal:** materiales del curso Análisis Multivariado I (Universidad ESAN), presentación del Proyecto Integrador, especialmente la estructura del proyecto (página 4), el caso de bebidas energéticas (páginas 6–10), y el diccionario de variables entregado con la base. Los resultados numéricos se calcularon directamente desde la base Excel suministrada.
