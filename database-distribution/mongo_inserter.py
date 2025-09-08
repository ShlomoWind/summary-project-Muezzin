from pymongo import MongoClient
from bson.binary import Binary

class MongoConnector:
    def __init__(self,url,db_name,collection_name):
        self.client = MongoClient(url)
        self.db = self.client[db_name]
        self.coll = self.db[collection_name]

class WavInserter:
    def __init__(self,mongo_connection:MongoConnector):
        self.conn = mongo_connection

    def read_wav(self,file_path,unique_id):
        with open(file_path, 'rb') as f:
            wav_data = f.read()
            document = {
                "unique_id": unique_id,
                "content_type": "audio/wav",
                "wav_file": Binary(wav_data)
            }
            self.conn.coll.insert_one(document)