from fastapi import FastAPI, HTTPException
from typing import Optional
import datetime


from api.risk_service import get_route_risk
from api.gear_service import analyze_route_with_ai

app = FastAPI(
    title="AeroRisk Platform API",
    description="Sistema de Evaluación de Riesgos Aéreos con Google GEAR",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "AeroRisk API está operativa. Usa /ai-risk para consultas."}


@app.get("/ai-risk")
def get_ai_risk_report(from_iata: str, to_iata: str):
    """
    Endpoint principal: Consulta BigQuery y genera un reporte con IA.
    """
    try:
        # 1. Consultar datos técnicos en BigQuery
        route_data = get_route_risk(from_iata, to_iata)

        if not route_data:
            raise HTTPException(status_code=404, detail="Ruta no encontrada en la base de datos.")

        # 2. Enviar los datos a la IA (GEAR) para el reporte de experto
        # Pasamos el diccionario completo que viene de BigQuery
        ai_report = analyze_route_with_ai(route_data)

        # 3. Construir la respuesta final unificada
        return {
            "meta": {
                "source": "BigQuery Data Warehouse",
                "intelligence": "Groq LLaMA 3.1 (Free AI)",
                "timestamp": datetime.datetime.now().isoformat()
            },
            "technical_data": {
                "route": f"{from_iata} → {to_iata}",
                "risk_score": route_data["risk_score"],
                "risk_level": route_data["risk_level"],
                "ai_recommendation": route_data["ai_recommendation"],
                "details": route_data["details"]
            },
            "ai_expert_report": ai_report
        }

    except Exception as e:
        return {
            "error": "Error interno en el servidor",
            "detail": str(e)
        }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)