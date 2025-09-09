from config.environments import MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME,UNIQUE_ID_TOPIC,KAFKA_ADDRESS
from utils.mongo_connector import MongoConnector
from manager import UpdateManager

if __name__ == "__main__":
    conn = MongoConnector(MONGO_URL, MONGO_DB_NAME, COLLECTION_NAME)
    UpdateManager(conn,UNIQUE_ID_TOPIC,KAFKA_ADDRESS).run()