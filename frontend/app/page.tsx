import React from 'react';

export default function Home() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1>MediFed XAI Resource Orchestrator</h1>
      <p>Decentralized Clinic Telemetry & Anomalies</p>
      <div style={{ border: '1px solid #ccc', padding: '1.5rem', marginTop: '2rem', borderRadius: '8px' }}>
        <h2>Active Anomalies Overview</h2>
        <ul>
          <li style={{ marginBottom: '1rem' }}>
            <strong>Clinic Alpha</strong> - Ventilator Shortage (Anomaly Score: 0.88) 
            <br/>
            <em>Recommended Action:</em> Reroute 20 units of ventilators
            <br/>
            <span style={{ color: 'orange', fontWeight: 'bold' }}>Status: Pending Slack HITL Approval</span>
          </li>
        </ul>
      </div>
    </div>
  );
}
