import json
from kafka import KafkaProducer

class Producer:
    def __init__(self,server_address):
        self.server_address = server_address
        self.producer = KafkaProducer(bootstrap_servers=[self.server_address],
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def publish(self,message,topic):
        self.producer.send(topic, value=message)
        self.producer.flush()
        print(f"Published message: {message}, \nto topic: {topic}")