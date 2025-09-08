import json
from kafka import KafkaConsumer
from utils.class_logger import Logger


class Consumer:
    def __init__(self,topic,server_address):
        self.logger = Logger.get_logger()
        self.topic = topic
        self.server_address = server_address
        try:
            self.consumer = KafkaConsumer(self.topic,
                                      bootstrap_servers=[self.server_address],
                                      value_deserializer=lambda v: json.loads(v.decode("utf-8")),
                                      consumer_timeout_ms=1000)
            self.logger.info("consumed data successfully")
        except Exception as e:
            self.logger.error(f"an error occurred while consumed data - {e}")