# 🌋 Dashboard de Demanda Sísmica y Aceleración Máxima del Suelo en el Perú (2019 – 2026)

## 📌 Descripción del Proyecto
Este proyecto implementa un **pipeline end-to-end de datos** para procesar, transformar y analizar los registros de **Aceleración Máxima del Suelo (PGA)** emitidos por la Red Sísmica Nacional del **Instituto Geofísico del Perú (IGP)** a través del servicio **ACELDAT_Perú**.

El objetivo es evaluar la intensidad y distribución espacial/temporal de la demanda sísmica generada por eventos de magnitud mayor o igual a $M4.5$, permitiendo identificar las regiones, distritos y estaciones acelerométricas expuestas a mayores niveles de riesgo o fuerza de sacudimiento.

---

## 🛠️ Tecnologías y Herramientas Utilizadas
* **Lenguaje de Programación:** Python 3.x (Pandas, NumPy) para automatización del flujo ETL, limpieza profunda de datos e ingeniería de características.
* **Business Intelligence (BI):** Power BI Desktop (DAX, Power Query) para el modelado de datos, diseño de KPIs y tablero interactivo.
* **Control de Versiones:** Git / GitHub para trazabilidad del código y documentación del proyecto[cite: 1, 3].
* **Fuente de Datos:** [Instituto Geofísico del Perú - IGP / Plataforma Nacional de Datos Abiertos][cite: 3]

---

## 📸 Vista del Dashboard Interactivo (Power BI)

![Dashboard de Demanda Sísmica](img/dashboard_preview.png)

---

## ⚙️ Arquitectura y Proceso ETL (Python)

El flujo de procesamiento implementado en `analisis.py` resuelve las anomalías de los datos crudos mediante las siguientes etapas:

1. **Ingeniería de Características:** 
   Se combinaron vectorialmente las tres componentes de aceleración sísmica ($Z$, $N-S$, $E-O$) para obtener la **Aceleración Máxima Resultante (PGA)**, el indicador técnico fundamental de sacudimiento del suelo:
   ```text
   PGA_RESULTANTE = sqrt(ACEL_VERTICAL^2 + ACEL_NORTE_SUR^2 + ACEL_ESTE_OESTE^2)

2. **Estandarización y Limpieza Temporal:**
   * Inferencia de fechas mediante respaldo cruzado entre `FECHA_EVENTO` y `FECHA_CORTE`[cite: 1].
   * Relleno automático de marcas de hora mediante formateo estricto de 6 dígitos (`HHMMSS`), reduciendo a **0 las fechas nulas (NaT)**[cite: 1].

3. **Formateo Geoespacial:**
   * Estandarización a 6 dígitos exactos del código de `UBIGEO` con ceros a la izquierda (`str.zfill(6)`) para permitir compatibilidad estricta con capas GIS y herramientas cartográficas del Perú[cite: 1].

---

## 📊 Principales Hallazgos 

* **Pico Histórico de Demanda Sísmica:** El departamento de **Lima** lideró la mayor demanda sísmica del periodo, registrando un pico máximo nacional de **514.49 cm/s²** en la estación de **Lurín (LURN)** durante el evento del 22 de junio de 2021[cite: 2].
* **Top Departamentos Afectados:**
  1. **Lima:** 514.49 cm/s²[cite: 2]
  2. **Ica:** 358.00 cm/s²[cite: 2]
  3. **Moquegua:** 332.00 cm/s²[cite: 2]
  4. **Ancash:** 294.00 cm/s²[cite: 2]
* **Comportamiento Promedio:** La aceleración promedio nacional se sitúa en **5.61 cm/s²**, lo que confirma un volumen constante de eventos leves/moderados con picos esporádicos de alta severidad en la franja costera[cite: 2].

---

## 📁 Estructura del Repositorio

```text
Analisis-Demanda-Sismica-Peru-IGP/
├── .gitignore                                   # Archivo de descarte de temporales y datos pesados[cite: 1]
├── ACELDAT_Peru_Procesado.csv                  # Dataset transformado, limpio y sin nulos[cite: 1]
├── IGP_ACELDAT_Peru_2019-2025_Diccionario...   # Diccionario de datos original[cite: 1]
├── analisis.py                                  # Script principal de automatización ETL[cite: 1]
├── dashboard.pbix                               # Archivo fuente del reporte en Power BI[cite: 1]
├── README.md                                    # Documentación del proyecto[cite: 3]
└── img/
    └── dashboard_preview.png                    # Captura del dashboard para la vista previa[cite: 3]
