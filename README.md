Drone Battery Health Monitoring System 🚁🔋


An end-to-end data engineering pipeline designed to monitor and analyze drone battery degradation in real-time. This project simulates telemetry data and visualizes battery health metrics to support predictive maintenance.

🚀 Project Overview
In the robotics and anti-drone industry, tracking battery health is critical for operational efficiency. This pipeline captures real-time data from drone simulators, processes it through a streaming broker, and visualizes it for actionable insights.

🛠 Tech Stack
Languages: Python

Data Streaming: Apache Kafka

Database: MySQL

Visualization: Power BI

Environment: VS Code



Power BI dashboard 







<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f60fa269-d196-40c4-8818-79c5b5fbf225" />

🏗 Pipeline Architecture
Producer: Simulates telemetry data (Cycle Index, Capacity) from drone units.

Kafka: Ingests high-velocity streaming data.

Consumer: Python-based script to process and clean data for storage.

Data Warehouse: MySQL database for structured data storage.

Dashboard: Power BI for real-time visualization of degradation trends.
