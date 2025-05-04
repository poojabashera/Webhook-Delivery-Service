import redis
import json
import time
import requests

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

def process_event(event):
    try:
        print(f"Sending event to {event['webhook_url']}...")
        response = requests.post(event["webhook_url"], json=event["payload"], timeout=5)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send event: {e}")

def run_worker():
    print("Worker started. Listening for events...")
    while True:
        _, event_data = r.blpop("event_queue")  # Blocking pop
        event = json.loads(event_data)
        process_event(event)
        time.sleep(1)

if __name__ == "__main__":
    run_worker()
