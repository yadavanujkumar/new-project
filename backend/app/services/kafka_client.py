import logging
import os
from confluent_kafka import Producer

logger = logging.getLogger(__name__)

class KafkaEventStreamer:
    """
    Produces telemetry and anomaly events to Apache Kafka for decentralized processing.
    """
    def __init__(self):
        bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        self.producer = Producer({"bootstrap.servers": bootstrap_servers})

    def publish_event(self, topic: str, payload: str):
        try:
            self.producer.produce(topic, payload.encode('utf-8'))
            self.producer.flush()
            logger.info(f"Published event to Kafka topic: {topic}")
        except Exception as e:
            logger.error(f"Failed to publish to Kafka: {e}")
