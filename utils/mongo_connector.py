from pymongo import MongoClient
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