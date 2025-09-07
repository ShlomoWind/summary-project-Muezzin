import json
from create_unique_id import UniqueId
from kafka import KafkaConsumer
from config.environments import KAFKA_ADDRESS,FIRST_JSON_TOPIC



class Consumer:
    def __init__(self,topic,server_address):
        self.unique_id = UniqueId
        self.topic = topic
        self.server_address = server_address
        self.consumer = KafkaConsumer(self.topic,
                                      bootstrap_servers=[self.server_address],
                                      value_deserializer=lambda v: json.loads(v.decode("utf-8")),
                                      consumer_timeout_ms=10000)

    def attach_id(self):
        for message in self.consumer:
            print(message)
            metadata = message.value['metadata']
            print(metadata)
            uniq_id = self.unique_id(metadata)
            message.value['_id'] = uniq_id
            print(message.value)


d = Consumer(FIRST_JSON_TOPIC,KAFKA_ADDRESS)
d.attach_id()