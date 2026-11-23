# Diccionario de variables — Caso Bebidas Energéticas RB

| Variable | Tipo de dato | Descripción | Rol en el modelo | Rango observado |
|---|---|---|---|---|
| año | Entero | Año calendario de la observación | Identificador temporal | 2010–2016 |
| semana | Entero | Número de semana ISO dentro del año | Identificador temporal | 1–53 |
| TotalvolmeRB | Continua | Volumen total de ventas de RB en la semana, en el panel Supermercado/Hipermercado | Variable dependiente (Y) | 17,924–214,708 |
| TotalPromosRB | Entero | Número total de acciones promocionales realizadas en la semana (suma de las 6 variables de tipo de promoción) | Predictor agregado; no usar junto con las 6 desagregadas porque existiría colinealidad perfecta | 8–688 |
| DispRB | Entero | Nº de acciones de Exhibición / Display (colocación destacada del producto, sin folleto ni descuento) | Predictor (X) | 4–594 |
| FollRB | Entero | Nº de acciones de Folleto (publicidad en encarte/catálogo del detallista) | Predictor (X) | 0–201 |
| DisfoRB | Entero | Nº de acciones combinadas de Display + Folleto (exhibición apoyada con publicidad simultánea) | Predictor (X) | 0–69 |
| CanexRB | Entero | Nº de acciones de Cantidad Extra (más producto por el mismo precio, ej. “20% gratis”) | Predictor (X) | 0–6 |
| LoteRB | Entero | Nº de acciones de Lote / Pack promocional (venta en pack o multipack a precio especial) | Predictor (X) | 0–96 |
| CupoRB | Entero | Nº de acciones de Cupón (descuento vía cupón redimible) | Predictor (X) | 0–3 |

## Selección de variables usada en el modelo

La regresión principal utiliza `TotalvolmeRB` como variable dependiente y `DispRB`, `FollRB`, `DisfoRB` y `LoteRB` como predictores. `CanexRB` y `CupoRB` se excluyen de la especificación estimada por su extrema concentración en cero; deben volver a evaluarse al disponer de más datos. `TotalPromosRB` es el total agregado de las seis promociones, por lo que no debe incluirse a la vez que las variables desagregadas.

**Fuente:** archivo de diccionario proporcionado para el Proyecto Integrador de Análisis Multivariado I.
