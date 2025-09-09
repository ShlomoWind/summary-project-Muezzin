from manager import PublisherManager
from config.environments import METADATA_JSON_TOPIC,FOLDER_PATH

if __name__ == "__main__":
    PublisherManager(FOLDER_PATH, METADATA_JSON_TOPIC).run()
