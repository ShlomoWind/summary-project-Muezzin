from utils.class_logger import Logger

class JsonExporter:
    def __init__(self,file_path, metadata):
        self.logger = Logger.get_logger()
        self.file_path = file_path
        self.metadata = metadata
        self.json_file = None

    def export_json(self):
        self.json_file = {'file path': str(self.file_path), 'metadata': self.metadata}
        self.logger.info("created the json file")
        return self.json_file