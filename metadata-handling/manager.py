from pathlib import Path
from metadata_retrieval import MetadataCreator
from json_builder import JsonExporter
from utils.publisher import Producer

TOPIC = ""
FOLDER_PATH = r"D:\Users\User\Desktop\podcasts"
KAFKA_PATH = "localhost:9092"

class Manager:
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.publisher = Producer(KAFKA_PATH)
        self.meta_creator = MetadataCreator
        self.json_build = JsonExporter


    def run(self):
        p = Path(self.folder_path)
        for item in p.iterdir():
            metadata =  self.meta_creator(item).create_metadata()
            print(metadata)
            jso = self.json_build(item,metadata).export_json()
            print(jso)