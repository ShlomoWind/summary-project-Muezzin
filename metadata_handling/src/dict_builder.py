from utils.class_logger import Logger

class DictExporter:
    def __init__(self,file_path, metadata):
        self.logger = Logger.get_logger()
        self.file_path = file_path
        self.metadata = metadata
        self.json_file = None

    def export_dict(self):
        try:
            self.json_file = {'file path': str(self.file_path), 'metadata': self.metadata}
            self.logger.info("created the json file")
            return self.json_file
        except Exception as e:
            self.logger.info(f"dict creation error: {e}")