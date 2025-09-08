# class BinaryConvert:
#     def __init__(self,file_name,binary_data):
#         self.file_name = file_name
#         self.binary_data = binary_data
#
#     def write_to_wav(self):
#         with open(f"{self.file_name}.wav", "wb") as f:
#             f.write(self.binary_data)
#             return f
#
#
#     document = collection.find_one({'_id': 'your_document_id'})
#     if document and 'audio_data' in document:
#         wav_binary_data = document['audio_data']