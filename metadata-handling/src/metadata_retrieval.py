from utils.src.class_logger import Logger
from pathlib import Path
import datetime

class MetadataCreator:
    def __init__(self,file_path):
        self.logger = Logger.get_logger()
        self.file_path = Path(file_path)
        self.metadata = None

    def create_metadata(self):
        try:
            if self.file_path.exists():
                self.metadata = {
                    "name": self.file_path.name,
                    "size_bytes": self.file_path.stat().st_size,
                    "creation_time": str(datetime.datetime.fromtimestamp(self.file_path.stat().st_ctime)),
                    "modification_time": str(datetime.datetime.fromtimestamp(self.file_path.stat().st_mtime)),
                }
                self.logger.info("metadata retrieval successful")
                return self.metadata
            else:
                self.logger.info("metadata retrieval failed")
                return f"File not found: {self.file_path}"
        except Exception as e:
            self.logger.error(f"an error occurred while trying to create metadata - {e}")