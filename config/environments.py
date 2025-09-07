import os

FIRST_JSON_TOPIC = os.getenv("FIRST_JSON_TOPIC","first_json_topic")
KAFKA_ADDRESS = os.getenv("KAFKA_ADDRESS","localhost:9092")
FOLDER_PATH = os.getenv("FOLDER_PATH",r"D:\Users\User\Desktop\podcasts")
MONGO_URL = os.getenv("MONGO_URL","mongodb://localhost:27017/")
ELASTICSEARCH = os.getenv("ELASTICSEARCH","http://localhost:9200")