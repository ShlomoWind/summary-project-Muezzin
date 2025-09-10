import speech_recognition as sr
from utils.class_logger import Logger

class BinaryTranscript:
    def __init__(self,binary_data,unique_id):
        self.binary_data = binary_data
        self.unique_id = unique_id
        self.logger = Logger.get_logger()

    def transcript(self):
        try:
            result = {'unique_id': self.unique_id}
            output_filename = 'temp_audio.wav'
            with open(output_filename, 'wb') as f:
                f.write(self.binary_data)
            self.logger.info(f"WAV file saved as {output_filename}")
            r = sr.Recognizer()
            with sr.AudioFile(output_filename) as source:
                audio = r.record(source)
                transcription = r.recognize_google(audio)
                result['transcription'] = transcription
            return result
        except Exception as e:
            self.logger.info(f"trascript creation error: {e}")