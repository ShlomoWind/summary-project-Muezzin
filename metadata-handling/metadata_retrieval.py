from pathlib import Path
import datetime

class MetadataCreator:
    def __init__(self,file_path):
        self.file_path = Path(file_path)
        self.metadata = None

    def create_metadata(self):
        if self.file_path.exists():
            self.metadata = {
                "name": self.file_path.name,
                "size_bytes": self.file_path.stat().st_size,
                "creation_time": datetime.datetime.fromtimestamp(self.file_path.stat().st_ctime),
                "modification_time": datetime.datetime.fromtimestamp(self.file_path.stat().st_mtime),
            }
            return self.metadata
        else:
            return f"File not found: {self.file_path}"