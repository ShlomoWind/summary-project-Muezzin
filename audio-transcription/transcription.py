from utils.mongo_connector import MongoConnector
from utils.class_logger import Logger
from config.environments import MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME
from binary_to_wav import BinaryTranscript


class Manager:
    def __init__(self,mongo_connection:MongoConnector):
        self.mongo_conn = mongo_connection
        self.logger =Logger.get_logger()
        self.transcript = BinaryTranscript


    def run(self):
        documents = self.mongo_conn.coll.find()
        for doc in documents:
            binary_data = doc['wav_file']
            unique_id = doc['unique_id']
            result = self.transcript(binary_data, unique_id).transcript()
            print(result)
            self.logger.info(f"created {result}")


c= MongoConnector(MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME)
m = Manager(c).run()


