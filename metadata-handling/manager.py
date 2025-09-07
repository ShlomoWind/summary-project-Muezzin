from pathlib import Path
from config.environments import KAFKA_ADDRESS
from metadata_retrieval import MetadataCreator
from json_builder import JsonExporter
from utils.publisher import Producer


class Manager:
    def __init__(self,folder_path,topic):
        self.folder_path = folder_path
        self.publisher = Producer(KAFKA_ADDRESS)
        self.meta_creator = MetadataCreator
        self.json_build = JsonExporter
        self.topic = topic


    def run(self):
        p = Path(self.folder_path)
        for item in p.iterdir():
            metadata =  self.meta_creator(item).create_metadata()
            print(metadata)
            jso = self.json_build(item,metadata).export_json()
            print(jso)
            self.publisher.publish(jso,self.topic)