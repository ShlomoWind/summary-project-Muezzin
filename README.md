#  summary-project-Muezzin
## There is still room for improvement....😜

---

## Project Structure

```
summary-project-Muazzin/
├── metadata-handling/
│   ├── src/
│   │    ├── main.py.py
│   │    ├── manager.py
│   │    ├── dict_builder.py
│   │    └── metadata_retrieval.py
│   └── Dockerfile
├── database-distribution/
│   ├── src/
│   │   ├── main.py
│   │   ├── manager.py
│   │   ├── create_unique_id.py
│   │   └── wav_to_binary.py
│   └── Dockerfile
├── audio-transcription/
│   ├── src/
│   │   ├── main.py
│   │   ├── manager.py
│   │   ├── binary_to-wav.py
│   │   ├── temp_audio.wav
│   └── Dockerfile
├── text_classification/
│   ├── deciphering.py
│   ├── identifying_matches.py
│   ├── level_attach.py
│   ├── manager.py
│   ├── percentage_calculation.py
│   └── words_lists
├── utils/
│   ├── publisher.py
│   ├── consumer.py
│   ├── class logger.py
│   └── mongo_connector.wav
├── config/
│   └── environments.py 
├── docker-compose.yaml
└── README.md
```

---

## Project Flow

1. The program uploads WAV files - podcasts to the system and sends them to Kafka as Jason with the path and metadata.
2. The following program listens to the specific topic in Kafka and extracts the information and generates a unique identifier based on the data, and publishes the metadata to Elastic and the binary file itself to Mongo, while simultaneously publishing the unique identifier to a different topic.
3. In the next step, the system listens to the topic and for each unique identifier that is published, the system retrieves the binary file from Mongo DB and transcribes the file and runs an identification against the lists of hostile words and assigns them risk percentages and a level of danger and updates all the data in Elastic according to the unique identifier.
4. The next step I was supposed to do was containerize everything and run it non-locally.
---

## Decisions

- I decided to do the transcription logic only after saving in Mongo
and perform a retrieval from Mongo and transcription,
and then update the elastic
The main reason is that transcription takes time and in large databases this is significant, so I will first send the metadata and only then update the transcription.
- My calculation of the risk percentage is based on the score obtained by dividing the text width by one hundred to increase the number (I didn't have time to adjust the calculation to be more accurate).
- The decision on the levels of danger was made based on a visual examination of the statistics and without in-depth thought due to lack of time.
---


## Tech Stack

- Python 3.10+
- ElasticSearch
- Mongo DB
- Kafka
- Kibana
- SpeechRecognition
---

## Contact

Project maintained by **Shlomo Wind**  
Feel free to fork, improve, and use in your own systems.