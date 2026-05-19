# s3_reader.py

import boto3
import json
import pandas as pd
from config import S3_CONFIG, S3_BUCKET, S3_PREFIX, TOPICS

# ── S3 Client ────────────────────────────────
s3_client = boto3.client("s3", **S3_CONFIG)


def list_s3_files(topic: str, date: str = None) -> list:
    """Topic ke saare files list karo."""

    prefix = f"{S3_PREFIX}/{topic}/"
    if date:
        prefix = f"{S3_PREFIX}/{topic}/{date}/"

    try:
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=prefix
        )
        files = []
        if "Contents" in response:
            for obj in response["Contents"]:
                files.append(obj["Key"])

        print(f"[S3] {topic}: {len(files)} files found")
        return files

    except Exception as e:
        print(f"[ERROR] List failed: {e}")
        return []


def read_s3_file(key: str) -> dict:
    """Single JSON file padhna."""
    try:
        response = s3_client.get_object(
            Bucket=S3_BUCKET,
            Key=key
        )
        content = response["Body"].read().decode("utf-8")
        return json.loads(content)

    except Exception as e:
        print(f"[ERROR] Read failed: {key} → {e}")
        return {}


def load_topic_data(topic: str, date: str = None) -> pd.DataFrame:
    """Topic ka saara data DataFrame mein load karo."""

    files   = list_s3_files(topic, date)
    records = []

    for file_key in files:
        data = read_s3_file(file_key)
        if data:
            records.append(data)

    if not records:
        print(f"[WARNING] No data: {topic}")
        return pd.DataFrame()

    df = pd.DataFrame(records)

    # Timestamp convert karo
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp").reset_index(drop=True)

    print(f"[LOADED] {topic}: {len(df)} records")
    return df


def load_all_topics(date: str = None) -> dict:
    """Saare topics ka data load karo."""

    all_data = {}
    for topic in TOPICS:
        df             = load_topic_data(topic, date)
        all_data[topic] = df

    return all_data


# ── Test ─────────────────────────────────────
if __name__ == "__main__":
    print("\n[TEST] S3 Reader Starting...")
    print("="*40)

    data = load_all_topics()

    for topic, df in data.items():
        print(f"\nTopic: {topic}")
        print(f"Records: {len(df)}")
        if not df.empty:
            print(df.head(2))