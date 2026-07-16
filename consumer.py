from kafka import KafkaConsumer
import json
import mysql.connector
import sys

# MySQL connection (Updated with 127.0.0.1)
try:
    conn = mysql.connector.connect(
        host='127.0.0.1', 
        user='root', 
        password='rootpassword', 
        database='drone_db', 
        port=3307
    )
    cursor = conn.cursor()
    print("Database se connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    sys.exit(1)

# Kafka Consumer setup
consumer = KafkaConsumer(
    'drone_telemetry', 
    bootstrap_servers=['localhost:9092'], 
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer waiting for data...")

for message in consumer:
    try:
        data = message.value
        # Database mein insert
        query = "INSERT INTO battery_logs (battery_id, cycle_index, capacity) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['battery_id'], data['cycle_index'], data['capacity']))
        conn.commit()
        print(f"Saved to DB: {data['battery_id']} - Cycle: {data['cycle_index']}")
    except Exception as e:
        print(f"Data save karne mein error: {e}")