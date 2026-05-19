import json
from kafka import KafkaProducer
from datetime import datetime
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x:
        json.dumps(x).encode('utf-8')
)

while True:
    # Data Banao
    temperature_data = {
        'timestamp': datetime.now().isoformat(),
        'sensor_id': "temp-001",
        'value'    : random.uniform(20, 100),
        'unit'     : "celsius"
    }
    speed_data = {
        'timestamp': datetime.now().isoformat(),
        'sensor_id': "speed-001",
        'value'    : random.randint(0, 1000),
        'unit'     : "rpm"
    }
    pressure_data = {
        'timestamp': datetime.now().isoformat(),
        'sensor_id': "press-001",
        'value'    : random.uniform(1, 10),
        'unit'     : "bar"
    }

    # Kafka Ko Bhejo
    producer.send('temperature-data', temperature_data)
    producer.send('speed-data', speed_data)
    producer.send('pressure-data', pressure_data)

    # Print Karo
    print(f"Bheja: {temperature_data}")
    print(f"Bheja: {pressure_data}")
    print(f"Bheja: {speed_data}")

    # 2 Second Ruko
    time.sleep(2)