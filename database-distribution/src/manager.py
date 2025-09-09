from wav_to_binary import WavConverter
from utils.src.mongo_connector import MongoConnector
from elasticsearch import Elasticsearch
from create_unique_id import UniqueId
from utils.src.consumer import Consumer
from utils.src.class_logger import Logger
from config.environments import INDEX_NAME

class ConsumerManager:
    def __init__(self,topic,address,mongo_url,db_name,coll_name,elastic):
        self.consumer = Consumer(topic,address).consumer
        self.mongo_connector = MongoConnector(mongo_url,db_name,coll_name)
        self.mongo_inserter = WavConverter(self.mongo_connector)
        self.es = Elasticsearch(elastic)
        self.unique_id = UniqueId
        self.logger = Logger.get_logger()

    def run(self):
        data_for_es = {}
        try:
            for message in self.consumer :
                metadata = message.value['metadata']
                uniq_id = self.unique_id(metadata).generate_dict_hash()
                self.logger.info("manager crete unique_id")
                message.value['unique_id'] = uniq_id
                data_for_es["unique_id"] = uniq_id
                data_for_es["metadata"] = message.value["metadata"]
                self.logger.info("manager create json to insert in es")
                self.es.index(index=INDEX_NAME, document=data_for_es)
                self.logger.info("manager inserted in es")
                self.mongo_inserter.read_wav(message.value['file path'],uniq_id)
                self.logger.info("manager inserted in mongo")
            self.consumer.close()
            self.logger.info("consumer closed!")
        except Exception as e:
            self.logger.error(f"an error occurred while retrieving the data and sending it to the databases - {e}")