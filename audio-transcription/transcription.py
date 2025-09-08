import openai

key = "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"
openai.api_key = key

audio_path = r"D:\Users\User\Desktop\podcasts\download (1).wav"


with open(audio_path, "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        model = 'wisper-1',
        file = audio_file,
        respons_format = "text",
        language = "en")
    print("Transcribed Text:", transcript)
