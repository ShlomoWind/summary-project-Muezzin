from utils.mongo_connector import MongoConnector
from utils.class_logger import Logger
from binary_to_wav import BinaryTranscript
from elasticsearch import Elasticsearch
from utils.consumer import Consumer
from text_classification.manager import PercentManager
from config.environments import ELASTICSEARCH,INDEX_NAME

trans_field_name = 'transcription'
percent_field_name = 'bds_percent'
thresh_field_name = 'threshold'
level_field_name = 'bds_threat_level'

class UpdateManager:
    def __init__(self,mongo_connection:MongoConnector,topic,address):
        self.es = Elasticsearch(ELASTICSEARCH)
        self.consumer = Consumer(topic,address).consumer
        self.mongo_conn = mongo_connection
        self.logger =Logger.get_logger()
        self.transcript = BinaryTranscript
        self.classify_text = PercentManager

    def run(self):
        try:
            for message in self.consumer:
                my_unique_id = message.value
                self.logger.info(f"consumed id: {my_unique_id}")
                doc = self.mongo_conn.coll.find_one({'unique_id': my_unique_id })
                self.logger.info(f"retrieving the document")
                binary_data = doc['wav_file']
                result = self.transcript(binary_data, my_unique_id).transcript()
                self.logger.info(f"created dict of result: {result}")
                classified = self.classify_text(result['transcription']).run()
                level = classified.level
                percent = classified.percent
                is_dangers = classified.is_dangers
                self.es.update(index=INDEX_NAME,id=my_unique_id,body={
                    "doc": {trans_field_name:result['transcription'],
                            percent_field_name:percent,
                            level_field_name:level,
                            thresh_field_name:is_dangers}
                })
                # self.es_update(result['unique_id'],result['transcription'],percent,level,is_dangers).update_by_query()
                self.logger.info("update elastic \n===============")
        except Exception as e:
            self.logger.error(f"an error occurred while updating elastic - {e}")