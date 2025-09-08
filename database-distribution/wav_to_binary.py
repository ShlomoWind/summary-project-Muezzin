from bson.binary import Binary
from utils.class_logger import Logger

class WavConverter:
    def __init__(self,mongo_connection):
        self.conn = mongo_connection
        self.logger = Logger.get_logger()

    def read_wav(self,file_path,unique_id):
        try:
            with open(file_path, 'rb') as f:
                wav_data = f.read()
                document = {
                    "unique_id": unique_id,
                    "content_type": "audio/wav",
                    "wav_file": Binary(wav_data)
                }
                self.logger.info("binary reading and dictionary preparation was successful")
                self.conn.coll.insert_one(document)
                self.logger.info("the dictionary was successfully added to the collection")
        except Exception as e:
            self.logger.error(f"an error occurred while uploading the file to Mongo - {e}")