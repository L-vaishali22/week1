# config.py

# ── LocalStack S3 Config ─────────────────────
S3_CONFIG = {
    "endpoint_url"          : "http://localhost:4566",
    "aws_access_key_id"     : "test",
    "aws_secret_access_key" : "test",
    "region_name"           : "us-east-1"
}

S3_BUCKET = "sms-factory-data-lake"
S3_PREFIX = "factory-data"

TOPICS = [
    "temperature-data",
    "pressure-data",
    "speed-data"
]

UNITS = {
    "temperature-data": "°C",
    "pressure-data"   : "Bar",
    "speed-data"      : "RPM"
}

ANOMALY_THRESHOLD = 2.0