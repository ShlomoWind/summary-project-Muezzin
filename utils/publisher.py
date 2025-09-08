import json
from kafka import KafkaProducer
from utils.class_logger import Logger

class Producer:
    def __init__(self,server_address):
        self.logger = Logger.get_logger()
        self.server_address = server_address
        self.producer = KafkaProducer(bootstrap_servers=[self.server_address],
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def publish(self,message,topic):
        try:
            self.producer.send(topic, value=message)
            self.producer.flush()
            self.logger.info(f"Published message: {message} ,to topic: {topic}")
        except Exception as e:
            self.logger.error(f"an error occurred while published message - {e}")