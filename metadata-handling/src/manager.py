from pathlib import Path
from config.environments import KAFKA_ADDRESS
from metadata_retrieval import MetadataCreator
from dict_builder import DictExporter
from utils.src.publisher import Producer
from utils.src.class_logger import Logger

class PublisherManager:
    def __init__(self,folder_path,topic):
        self.folder_path = folder_path
        self.publisher = Producer(KAFKA_ADDRESS)
        self.meta_creator = MetadataCreator
        self.dict_build = DictExporter
        self.topic = topic
        self.logger = Logger.get_logger()

    def run(self):
        try:
            p = Path(self.folder_path)
            for item in p.iterdir():
                metadata =  self.meta_creator(item).create_metadata()
                self.logger.info(f"manager created metadata {metadata}")
                json = self.dict_build(item,metadata).export_dict()
                self.logger.info(f"manager created json {json}")
                self.publisher.publish(json,self.topic)
                self.logger.info(f"manager published meta json to kafka")
        except Exception as e:
            self.logger.error(f"an error occurred while sending metadata to Kafka - {e}")