from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class TelemetryData(BaseModel):
    clinic_id: str = Field(..., description="Unique identifier for the decentralized clinic.")
    resource_type: str = Field(..., description="Type of resource (e.g., ventilators, ICU beds).")
    current_capacity: int = Field(..., ge=0)
    projected_demand: int = Field(..., ge=0)

class AnomalyPrediction(BaseModel):
    id: str
    clinic_id: str
    anomaly_score: float
    shap_explanation: Dict[str, Any]
    recommended_action: str
    hitl_approved: bool
