CREATE TABLE machine_data (
    id SERIAL PRIMARY KEY,

    timestamp TIMESTAMP,

    machine_id VARCHAR(20),

    shift VARCHAR(20),

    operator_name VARCHAR(50),

    production_count INT,

    passed_count INT,

    failed_count INT,

    temperature FLOAT,

    pressure FLOAT,

    vibration FLOAT,

    downtime_minutes INT,

    machine_status VARCHAR(20),

    failure_type VARCHAR(50)
);

