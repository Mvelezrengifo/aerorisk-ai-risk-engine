import os
from openai import OpenAI

# 🔹 Leer la clave desde .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "NO_KEY_FOUND")

# 🔹 Inicializar cliente OpenAI/Groq
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def analyze_route_with_ai(route_data):
    try:
        prompt = f"""
Eres un analista profesional de riesgo aeronáutico.

REGLAS:
- Usa SOLO los datos proporcionados
- NO agregues ejemplos ni descripciones adicionales
- NO infieras condiciones específicas (clima, tráfico, etc.)
- Sé técnico, preciso y directo

DATOS:
Ruta: {route_data['route']}
Nivel: {route_data['risk_level']}
Puntaje: {route_data['risk_score']}
Recomendación base: {route_data['ai_recommendation']}

FORMATO:

Analisis del Riesgo:
(Explica el nivel basándote únicamente en el puntaje y la recomendación)

Interpretacion:
(Qué implica operativamente ese nivel de riesgo, sin ejemplos externos)

Recomendacion Operacional:
(Acción concreta alineada con la recomendación base)
"""
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # 🔥 Modelo Groq bueno
            messages=[
                {"role": "system", "content": "Eres experto en análisis de riesgo aeronáutico."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error en IA: {str(e)}"