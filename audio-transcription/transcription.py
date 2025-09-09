from utils.mongo_connector import MongoConnector
import speech_recognition as sr
from config.environments import MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME

class MongoFetch:
    def __init__(self,mongo_connection:MongoConnector):
        self.mongo_conn = mongo_connection

    def trascripter(self,binary_data,unique_id):
        result = {'unique_id': unique_id}
        output_filename = 'temp_audio.wav'
        with open(output_filename, 'wb') as f:
            f.write(binary_data)
        print(f"WAV file saved as {output_filename}")
        r = sr.Recognizer()
        with sr.AudioFile(output_filename) as source:
            audio = r.record(source)
            transcription = r.recognize_google(audio)
            result['transcription'] = transcription
        return result

    def manager(self):
        documents = self.mongo_conn.coll.find()
        for doc in documents:
            binary_data = doc['wav_file']
            unique_id = doc['unique_id']
            result = self.trascripter(binary_data,unique_id)
            print(result)



c= MongoConnector(MONGO_URL,MONGO_DB_NAME,COLLECTION_NAME)
m = MongoFetch(c).manager()


