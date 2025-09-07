from manager import Manager
from config.environments import FIRST_JSON_TOPIC,FOLDER_PATH

if __name__ == "__main__":
    Manager(FOLDER_PATH,FIRST_JSON_TOPIC).run()
