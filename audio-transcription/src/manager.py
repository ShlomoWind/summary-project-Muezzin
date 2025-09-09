from utils.src.mongo_connector import MongoConnector
from utils.src.class_logger import Logger
from binary_to_wav import BinaryTranscript
from elastic_update import ElasticUpdate

class UpdateManager:
    def __init__(self,mongo_connection:MongoConnector):
        self.mongo_conn = mongo_connection
        self.logger =Logger.get_logger()
        self.es_update = ElasticUpdate
        self.transcript = BinaryTranscript

    def run(self):
        documents = self.mongo_conn.coll.find()
        for doc in documents:
            binary_data = doc['wav_file']
            unique_id = doc['unique_id']
            result = self.transcript(binary_data, unique_id).transcript()
            self.logger.info(f"created dict of result: {result}")
            self.es_update(result['unique_id'],result['transcription']).update_by_query()
            self.logger.info("update elastic")