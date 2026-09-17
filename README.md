# FTTH Data Analysis

Proyecto de análisis y procesamiento de datos operativos de una red FTTH/GPON, desarrollado como una versión demostrativa y anonimizada de procesos de análisis de datos realizados en un entorno profesional.

> **Nota:** Los datos incluidos en este repositorio son completamente ficticios y fueron creados únicamente con fines demostrativos. No se utilizan datos reales, información de clientes ni información confidencial.

---

##  Objetivo

Desarrollar un flujo reproducible para procesar información de una red FTTH/GPON y generar indicadores relacionados con:

- Potencia óptica.
- Posibles degradaciones.
- Tipos de alarmas.
- Distribución de alarmas por puerto.
- Resúmenes para análisis técnico.

---

##  Flujo del proyecto

```text
Datos CSV
   ↓
Carga y limpieza
   ↓
Procesamiento con Pandas
   ↓
Análisis de potencia
   ↓
Detección de degradación
   ↓
Análisis de alarmas
   ↓
Generación de resultados
   ↓
Reportes gráficos

Tecnologías utilizadas
Python
Pandas
NumPy
Matplotlib
CSV
Git
GitHub

FTTH-DATA-ANALYSIS/
│
├── data/
│   ├── raw/
│   │   └── ftth_sample.csv
│   │
│   └── processed/
│       ├── alarm_summary.csv
│       ├── alarms_by_port.csv
│       ├── degradation_analysis.csv
│       └── power_summary.csv
│
├── reports/
│   ├── alarm_distribution.png
│   └── average_power_by_port.png
│
├── src/
│   ├── data_processing.py
│   ├── power_analysis.py
│   ├── alarm_analysis.py
│   ├── generate_sample_data.py
│   ├── create_report.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt

Funcionalidades
1. Limpieza de datos

El proyecto realiza una limpieza básica de los datos:

Normalización de nombres de columnas.
Eliminación de registros duplicados.
Identificación de valores nulos.
Generación de un resumen del dataset.
2. Análisis de potencia óptica

Se calculan estadísticas de potencia por puerto:

Valor mínimo.
Valor máximo.
Promedio.
Mediana.

También se identifican registros que presentan valores de potencia por debajo de un umbral demostrativo.

3. Análisis de alarmas

Se generan indicadores sobre:

Cantidad de alarmas por tipo.
Cantidad de alarmas por puerto.
Distribución de eventos.
4. Generación de reportes

Los resultados procesados se almacenan en archivos CSV y se generan gráficos mediante Matplotlib.

**Resultados de ejemplo

El dataset demostrativo contiene inicialmente 500 registros.

Después del proceso de limpieza se obtuvieron:

499 registros
3 columnas
0 valores nulos
56 registros identificados para revisión por posible degradación

Distribución de eventos:

Sin alarma: 323
Baja potencia: 74
Intermitencia: 51
Pérdida de señal: 51

Estos resultados corresponden exclusivamente al dataset ficticio incluido en el repositorio.

**Reportes
Distribución de alarmas

Potencia óptica promedio por puerto
