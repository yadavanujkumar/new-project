from fastapi import APIRouter, HTTPException
from app.domain.models import TelemetryData, AnomalyPrediction
from app.services.xai import XAIEngine
from app.services.slack_hitl import SlackHITLManager
from app.services.kafka_client import KafkaEventStreamer
import uuid
import numpy as np

router = APIRouter()
xai_engine = XAIEngine()
hitl_manager = SlackHITLManager()
kafka_client = KafkaEventStreamer()

@router.post("/telemetry", response_model=AnomalyPrediction)
def process_telemetry(data: TelemetryData):
    # Simulate agentic anomaly detection
    is_anomaly = data.projected_demand > data.current_capacity * 1.2
    anomaly_score = 0.88 if is_anomaly else 0.12
    
    prediction_id = str(uuid.uuid4())
    explanation = xai_engine.explain_prediction(np.array([data.current_capacity, data.projected_demand]))
    
    action = f"Reroute 20 units of {data.resource_type} to {data.clinic_id}" if is_anomaly else "None"
    
    prediction = AnomalyPrediction(
        id=prediction_id,
        clinic_id=data.clinic_id,
        anomaly_score=anomaly_score,
        shap_explanation=explanation,
        recommended_action=action,
        hitl_approved=False
    )

    kafka_client.publish_event("telemetry-events", prediction.model_dump_json())

    if is_anomaly:
        hitl_manager.request_approval(prediction_id, action)
        
    return prediction
