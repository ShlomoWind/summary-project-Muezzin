from mongo_inserter import MongoConnector,WavInserter
from elasticsearch import Elasticsearch
from create_unique_id import UniqueId
from config.environments import KAFKA_ADDRESS,FIRST_JSON_TOPIC,ELASTICSEARCH,MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME
from utils.consumer import Consumer

class ConsumerManager:
    def __init__(self):
        self.consumer = Consumer(FIRST_JSON_TOPIC,KAFKA_ADDRESS).consumer
        self.mongo_connector = MongoConnector(MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME)
        self.mongo_inserter = WavInserter(self.mongo_connector)
        self.es = Elasticsearch(ELASTICSEARCH)
        self.unique_id = UniqueId

    def run(self):
        data_for_es = {}
        for message in self.consumer :
            print(f"message.value:{message.value}")
            metadata = message.value['metadata']
            print(f"metadata:{metadata}")
            uniq_id = self.unique_id(metadata).generate_dict_hash()
            message.value['_id'] = uniq_id
            print(f"message.value with unique:{message.value}")
            data_for_es["unique_id"] = uniq_id
            data_for_es["metadata"] = message.value["metadata"]
            print(f"data for elastic {data_for_es}")
            self.es.index(index="test", document=data_for_es)
            print("inserted_to_elastic")
            self.mongo_inserter.read_wav(message.value['file path'],uniq_id)