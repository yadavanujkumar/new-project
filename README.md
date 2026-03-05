# MediFed-XAI-Resource-Orchestrator

A federated agentic platform predicting healthcare resource anomalies across decentralized clinics. Autonomous agents analyze edge telemetry, utilizing PySyft for privacy-preserving federated learning to propose SHAP/LIME-backed medical resource rerouting. All actions require strict Human-In-The-Loop (HITL) approval via Slack, with zero-trust model updates cryptographically signed and logged for auditability.

## Architecture
- **Frontend**: Next.js (TypeScript, React)
- **Backend**: FastAPI (Python)
- **Event Streaming**: Apache Kafka
- **Federated Learning**: PySyft (Simulated decentralization)
- **Explainable AI (XAI)**: SHAP & LIME
- **Infrastructure**: Terraform, AWS SageMaker
- **Integration**: Slack API for HITL

## Setup
1. Ensure Docker and Docker Compose are installed.
2. Run `docker-compose up --build` to start Zookeeper, Kafka, Backend, and Frontend.
3. Access Frontend at `http://localhost:3000`
4. Access Backend API Docs at `http://localhost:8000/docs`

## Domain-Driven Design & Clean Architecture
The backend is structured into `api`, `domain`, and `services` layers ensuring separation of concerns and testability.
