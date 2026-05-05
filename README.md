# Smart-Factory-Monitoring-System
Real-time industrial monitoring dashboard using Grafana, PostgreSQL, and Python
# Smart Factory Monitoring Dashboard

## Overview
This project is a real-time industrial monitoring dashboard built using Grafana, PostgreSQL, and Python.

## Features
- Real-time machine monitoring
- KPI cards
- Production analytics
- Failure analysis
- Alerts and thresholds
- Shift-wise performance analysis
- Machine downtime tracking

## Technologies Used
- Grafana
- PostgreSQL
- Python

## Database Schema
The PostgreSQL database stores:
- machine temperature
- pressure
- vibration
- production count
- machine status
- failure types
- shift information


The data is continuously inserted using a Python live data generator.

## Workflow
Python Live Data Generator → PostgreSQL Database → Grafana Dashboard

## Project Structure

Smart_Factory_Project/
│
├── live_factory_data.py
├── database_schema.sql
├── project_explanation.txt
└── screenshots/

## Project Purpose
This project simulates an Industry 4.0 smart factory monitoring system using live generated industrial sensor data.

## Future Improvements
- IoT sensor integration
- MQTT live streaming
- AI-based predictive maintenance
- Cloud deployment
- Docker support
- PLC connectivity

## Dashboard Screenshots
<img width="1919" height="965" alt="Screenshot 2026-05-05 154707" src="https://github.com/user-attachments/assets/78e49261-ae01-46fc-9dc8-a06bd77fa945" />
<img width="1919" height="885" alt="Screenshot 2026-05-05 154719" src="https://github.com/user-attachments/assets/967f278c-39f3-4f57-8e4c-0b4ea7132ac2" />
<img width="1919" height="976" alt="Screenshot 2026-05-05 154741" src="https://github.com/user-attachments/assets/385db54d-4ebd-43a7-8631-3ba207c606d4" />

## Author

Pooja Naidu
