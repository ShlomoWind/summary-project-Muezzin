from utils.class_logger import Logger
import hashlib
import json

class UniqueId:
    def __init__(self,data):
        self.logger = Logger.get_logger()
        self.data_dict = data

    def generate_dict_hash(self):
        try:
            canonical_string = json.dumps(self.data_dict, sort_keys=True, ensure_ascii=False)
            encoded_data = canonical_string.encode('utf-8')
            unique_id = hashlib.sha256(encoded_data).hexdigest()
            self.logger.info("unique ID creation was successful")
            return unique_id
        except Exception as e:
            self.logger.error(f"an error occurred while generating a unique identifier - {e}")