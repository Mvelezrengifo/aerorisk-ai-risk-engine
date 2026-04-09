🚀 AeroRisk Intelligence Platform
AeroRisk es una plataforma global de data engineering + AI diseñada para evaluar riesgos aeronáuticos en rutas de vuelo. Combina datos climáticos históricos, tráfico aéreo real y un motor de riesgo avanzado para ofrecer análisis en tiempo real y recomendaciones operacionales confiables.

🧩 Arquitectura
Data Layer: Google BigQuery (procesamiento de 30+ años de datos climáticos)

Backend API: FastAPI en Python (endpoints /health y /ai-risk)

AI Layer: Groq Cloud – LLaMA 3.1 (interpretación y recomendaciones)

Dashboard (Diseñado): capa visual modular para mostrar niveles de riesgo y rutas, omitida en producción por confidencialidad de datos de la aerolínea.

📊 Motor de Riesgo
Clasifica rutas en tres niveles:

LOW → condiciones óptimas

MEDIUM → operación con precaución

CRITICAL → riesgo alto, requiere reevaluación

Ejemplo:

Código
Route: ASF > KZN  
Score: 91.54  
Risk: CRITICAL  
Recommendation: Route reassessment required
🌐 Fuentes de Datos
OpenSky Network → tráfico aéreo global en tiempo real

NOAA → datasets climáticos históricos

⚡ Tecnologías Utilizadas
Backend: FastAPI

Data Warehouse: BigQuery

AI: Groq LLaMA 3.1

Lenguajes: Python 3.10+

Librerías: Pandas, NumPy, PyArrow, xarray

🎯 Objetivo Profesional
AeroRisk está diseñado como un flagship project para demostrar:

Escalabilidad cloud-native

Integración AI en pipelines de datos

Documentación técnica reproducible

Impacto en decisiones críticas de aviación

## 📖 Documentación Técnica
El manual completo de arquitectura, endpoints y escenarios de riesgo está disponible aquí:  
[AeroRisk Technical & Intelligence Manual](https://github.com/Mvelezrengifo/aerorisk-ai-risk-engine/blob/main/notebooks/aerorisk_manual.pdf.pdf)
