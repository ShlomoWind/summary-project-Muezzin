import hashlib
import json

class UniqueId:
    def __init__(self,data):
        self.data_dict = data

    def generate_dict_hash(self):
        canonical_string = json.dumps(self.data_dict, sort_keys=True, ensure_ascii=False)
        encoded_data = canonical_string.encode('utf-8')
        unique_id = hashlib.sha256(encoded_data).hexdigest()
        return unique_id

