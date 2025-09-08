from mongo_inserter import MongoConnector,WavInserter
from elasticsearch import Elasticsearch
from create_unique_id import UniqueId
from utils.consumer import Consumer

class ConsumerManager:
    def __init__(self,topic,address,mongo_url,db_name,coll_name,elastic):
        self.consumer = Consumer(topic,address).consumer
        self.mongo_connector = MongoConnector(mongo_url,db_name,coll_name)
        self.mongo_inserter = WavInserter(self.mongo_connector)
        self.es = Elasticsearch(elastic)
        self.unique_id = UniqueId

    def run(self):
        data_for_es = {}
        for message in self.consumer :
            metadata = message.value['metadata']
            uniq_id = self.unique_id(metadata).generate_dict_hash()
            message.value['unique_id'] = uniq_id
            data_for_es["unique_id"] = uniq_id
            data_for_es["metadata"] = message.value["metadata"]
            print("=========")
            print(f"data for elastic {data_for_es}")
            self.es.index(index="test", document=data_for_es)
            print("inserted_to_elastic")
            self.mongo_inserter.read_wav(message.value['file path'],uniq_id)
            print("inserted to mongo")