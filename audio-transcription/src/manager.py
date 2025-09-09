from utils.mongo_connector import MongoConnector
from utils.class_logger import Logger
from binary_to_wav import BinaryTranscript
from elastic_update import ElasticUpdate
from utils.consumer import Consumer

class UpdateManager:
    def __init__(self,mongo_connection:MongoConnector,topic,address):
        self.consumer = Consumer(topic,address).consumer
        self.mongo_conn = mongo_connection
        self.logger =Logger.get_logger()
        self.es_update = ElasticUpdate
        self.transcript = BinaryTranscript

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
                self.es_update(result['unique_id'],result['transcription']).update_by_query()
                self.logger.info("update elastic \n===============")
        except Exception as e:
            self.logger.error(f"an error occurred while updating elastic - {e}")