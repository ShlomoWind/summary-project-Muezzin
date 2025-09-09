import base64

class Decoder:
    def __init__(self,code):
        self.code = code

    def decoding_code(self):
        to_bytes = base64.b64decode(self.code)
        result = to_bytes.decode("utf-8")
        return result.split(',')