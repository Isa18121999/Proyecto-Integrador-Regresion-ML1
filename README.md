# Proyecto Integrador – Modelo de Regresión RB

**Curso:** Análisis Multivariado I  
**Carrera:** Ingeniería de Tecnología de Información y Sistemas  
**Caso:** Bebidas energéticas RB  
**Técnica:** Regresión lineal múltiple

## Objetivo
Analizar la relación entre las promociones comerciales y el volumen semanal de ventas de bebidas energéticas RB, con el propósito de aportar evidencia para la toma de decisiones de marketing.

## Estructura
- `data/`: base de regresión y diccionario de variables.
- `docs/`: informe académico y material del curso.
- `src/`: scripts reproducibles de análisis.
- `results/`: resumen del modelo y resultados tabulares.
- `figures/`: gráficos del EDA y diagnóstico.

## Ejecución
Instalar Python 3 y las dependencias:

```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy openpyxl
```

Ejecutar:

```bash
python src/run_analysis.py
```

## Nota metodológica
El informe presenta el modelo y sus diagnósticos. Se identifican autocorrelación y heterocedasticidad en los residuos; por ello, las asociaciones estimadas no deben interpretarse como efectos causales y se recomienda una especificación temporal con inferencia robusta.

## Entregables
Consulte `docs/Informe_Regresion_RB.docx`, el dataset y el diccionario en `data/`, además de los gráficos y resultados correspondientes.
