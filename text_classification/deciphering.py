import base64

from utils.class_logger import Logger


class Decoder:
    def __init__(self,code):
        self.code = code
        self.logger = Logger.get_logger()

    def decoding_code(self):
        to_bytes = base64.b64decode(self.code)
        result = to_bytes.decode("utf-8")
        self.logger.info("decoding code successfully")
        return result.split(',')