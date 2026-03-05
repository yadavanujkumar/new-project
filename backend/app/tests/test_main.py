from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_process_telemetry():
    payload = {
        "clinic_id": "clinic-alpha",
        "resource_type": "ventilators",
        "current_capacity": 10,
        "projected_demand": 15
    }
    response = client.post("/api/v1/telemetry", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["clinic_id"] == "clinic-alpha"
    assert data["anomaly_score"] > 0.8
    assert "shap_explanation" in data
