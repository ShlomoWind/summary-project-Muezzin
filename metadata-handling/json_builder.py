class JsonExporter:
    def __init__(self,file_path, metadata):
        self.file_path = file_path
        self.metadata = metadata
        self.json_file = None

    def export_json(self):
        self.json_file = {'file path': self.file_path, 'metadata': self.metadata}
        return self.json_file

