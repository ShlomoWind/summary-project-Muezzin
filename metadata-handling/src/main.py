from manager import PublisherManager
from config.environments import FIRST_JSON_TOPIC,FOLDER_PATH

if __name__ == "__main__":
    PublisherManager(FOLDER_PATH,FIRST_JSON_TOPIC).run()
