import os

METADATA_JSON_TOPIC = os.getenv("FIRST_JSON_TOPIC", "metadata_json_topic")
UNIQUE_ID_TOPIC = os.getenv("UNIQUE_ID_TOPIC", "unique_id_topic")
KAFKA_ADDRESS = os.getenv("KAFKA_ADDRESS","localhost:9092")
FOLDER_PATH = os.getenv("FOLDER_PATH",r"D:\Users\User\Desktop\podcasts")
MONGO_URL = os.getenv("MONGO_URL","mongodb://localhost:27017/")
ELASTICSEARCH = os.getenv("ELASTICSEARCH","http://localhost:9200")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME","last_podcasts")
COLLECTION_NAME = os.getenv("COLLECTION_NAME","last_podcast")
INDEX_NAME = os.getenv("ELASTIC_INDEX_NAME","last_muezzin")