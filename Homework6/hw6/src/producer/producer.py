import csv
import json
from kafka import KafkaProducer
from time import time

def preprocess_data(row):
    def to_number(value, type_func, default=0):
        """Convert a value to a number, handling empty strings and missing keys."""
        try:
            return type_func(value.strip()) if isinstance(value, str) and value.strip() else default
        except (ValueError, TypeError):
            return default  # Handles cases where conversion fails

    passenger_count = to_number(row.get('passenger_count', 0), int)

    return {
        'lpep_pickup_datetime': row.get('lpep_pickup_datetime'),
        'lpep_dropoff_datetime': row.get('lpep_dropoff_datetime'),
        'PULocationID': to_number(row.get('PULocationID'), int),
        'DOLocationID': to_number(row.get('DOLocationID'), int),
        'passenger_count': passenger_count,
        'trip_distance': to_number(row.get('trip_distance'), float),
        'tip_amount': to_number(row.get('tip_amount'), float),
    }


def main():
    # Create a Kafka producer
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Default serialization
    )

    csv_file = '/Users/yitian66/Documents/DE-Datacamp/Week6/hw6/green_tripdata_2019-10.csv'  # change to your CSV file path if needed
    topic_name = 'green-trips'

    t0 = time()

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Preprocess the row to ensure it has the correct columns
            processed_row = preprocess_data(row)

            # Send the processed data to Kafka topic "green-trips"
            producer.send(topic_name, value=processed_row)

    # Make sure any remaining messages are delivered
    producer.flush()

    t1 = time()

    took = t1 - t0
    print(f"It takes {took} seconds to send the entire dataset and flush")

    # Close the producer after sending all messages
    producer.close()

    print("All messages sent to Kafka")

if __name__ == "__main__":
    main()