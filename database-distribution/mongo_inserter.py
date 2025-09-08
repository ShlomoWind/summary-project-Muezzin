from pymongo import MongoClient
from bson.binary import Binary
from utils.class_logger import Logger

class MongoConnector:
    def __init__(self,url,db_name,collection_name):
        self.logger = Logger.get_logger()
        try:
            self.client = MongoClient(url)
            self.db = self.client[db_name]
            self.coll = self.db[collection_name]
            self.logger.info("the connection with Mongo was successfully established")
        except Exception as e:
                    self.logger.error(f"an error occurred while connect to mongo - {e}")


class WavInserter:
    def __init__(self,mongo_connection:MongoConnector):
        self.conn = mongo_connection

    def read_wav(self,file_path,unique_id):
        try:
            with open(file_path, 'rb') as f:
                wav_data = f.read()
                document = {
                    "unique_id": unique_id,
                    "content_type": "audio/wav",
                    "wav_file": Binary(wav_data)
                }
                self.conn.logger.info("binary reading and dictionary preparation was successful")
                self.conn.coll.insert_one(document)
                self.conn.logger.info("the dictionary was successfully added to the collection")
        except Exception as e:
            self.conn.logger.error(f"an error occurred while uploading the file to Mongo - {e}")