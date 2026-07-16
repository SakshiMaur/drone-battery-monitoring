import pandas as pd
import json
import time
from kafka import KafkaProducer
import sys

print("Script shuru ho gayi hai...") # Debug print

try:
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    print("Producer connect ho gaya!") # Debug print
except Exception as e:
    print(f"Producer connect nahi hua: {e}")
    sys.exit()

df = pd.read_csv('combined_battery_data.csv')
print(f"Total rows load hui: {len(df)}") # Debug print

for index, row in df.iterrows():
    data = row.to_dict()
    producer.send('drone_telemetry', value=data)
    print(f"Row {index} bheji gayi: {data['battery_id']}") # Ye dikhna chahiye
    time.sleep(1)