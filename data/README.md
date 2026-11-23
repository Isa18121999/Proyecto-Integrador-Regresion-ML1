# Datos del proyecto

- `BD_REGRESION.csv`: base del caso RB convertida desde el Excel original; contiene 360 observaciones semanales y las 10 columnas de la base.
- `DICCIONARIO_VARIABLES_RB.md`: descripción de las variables, su rol y la lógica de selección.

El diccionario define `TotalPromosRB` como suma de las seis variables de promoción, por lo que no debe combinarse con las seis categorías desagregadas en una misma regresión. La especificación principal utiliza `DispRB`, `FollRB`, `DisfoRB` y `LoteRB`; `CanexRB` y `CupoRB` se excluyen por su concentración extrema de ceros.
