from kafka import KafkaConsumer
import boto3
import json
from datetime import datetime
import time

# =====================
# CONFIGURATION
# =====================
KAFKA_BROKER = 'localhost:9092'
TOPICS = ['temperature-data', 'pressure-data', 'speed-data']
BUCKET_NAME = 'sms-factory-data-lake'

# =====================
# S3 CLIENT - LOCALSTACK
# =====================
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='ap-south-1'
)

try:
    s3_client.head_bucket(Bucket=BUCKET_NAME)
    print(f"✅ Bucket already exists: {BUCKET_NAME}")
except Exception:
    s3_client.create_bucket(Bucket=BUCKET_NAME)
    print(f"✅ Bucket created: {BUCKET_NAME}")

# =====================
# KAFKA CONSUMER - RETRY LOGIC
# =====================
consumer = None
while consumer is None:
    try:
        print("🔄 Kafka se connect ho raha hai...")
        consumer = KafkaConsumer(
            *TOPICS,
            bootstrap_servers=KAFKA_BROKER,
            auto_offset_reset='earliest',
            consumer_timeout_ms=10000,
            request_timeout_ms=30000,
            session_timeout_ms=10000,
            heartbeat_interval_ms=3000,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("✅ Kafka se connect ho gaya!")
    except Exception as e:
        print(f"❌ Connect nahi hua: {e}")
        print("⏳ 5 seconds mein retry...")
        time.sleep(5)

print("✅ Consumer Started - Waiting for messages...")

# =====================
# MAIN LOOP
# =====================
for message in consumer:
    topic = message.topic
    data = message.value
    timestamp = datetime.now().strftime('%Y-%m-%d')
    time_now = datetime.now().strftime('%H-%M-%S-%f')

    # S3 File Path
    file_key = f"factory-data/{topic}/{timestamp}/msg_{time_now}.json"

    # S3 Mein Save Karo
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=file_key,
        Body=json.dumps(data),
        ContentType='application/json'
    )

    print(f"✅ Saved | Topic: {topic} | File: {file_key}")