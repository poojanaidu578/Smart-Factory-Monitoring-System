import psycopg2
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()

# DATABASE CONNECTION
conn = psycopg2.connect(
    host="localhost",
    database="smart_factory",
    user="postgres",
    password="pooja123"
)

cur = conn.cursor()

machines = ['M101', 'M102', 'M103', 'M104']

shifts = ['Morning', 'Afternoon', 'Night']

statuses = ['Running', 'Idle', 'Stopped']

failures = [
    'None',
    'Crack',
    'Alignment Error',
    'Sensor Failure',
    'Overheating'
]

while True:

    machine = random.choice(machines)

    shift = random.choice(shifts)

    operator = fake.first_name()

    production = random.randint(80, 120)

    failed = random.randint(0, 10)

    passed = production - failed

    temperature = random.uniform(60, 95)

    pressure = random.uniform(20, 40)

    vibration = random.uniform(0.1, 5.0)

    downtime = random.randint(0, 20)

    status = random.choice(statuses)

    failure = random.choice(failures)

    # REALISTIC INDUSTRIAL LOGIC

    if temperature > 90:
        status = "Stopped"
        downtime = random.randint(10, 40)
        failure = "Overheating"

    query = """
    INSERT INTO machine_data (
        timestamp,
        machine_id,
        shift,
        operator_name,
        production_count,
        passed_count,
        failed_count,
        temperature,
        pressure,
        vibration,
        downtime_minutes,
        machine_status,
        failure_type
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        datetime.now(),
        machine,
        shift,
        operator,
        production,
        passed,
        failed,
        temperature,
        pressure,
        vibration,
        downtime,
        status,
        failure
    )

    cur.execute(query, values)

    conn.commit()

    print("Inserted Live Data")

    time.sleep(2)