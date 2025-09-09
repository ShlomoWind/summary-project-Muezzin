#  summary-project-Muezzin
## It's still in writing - don't treat it as such😜
I decided to do the transcription logic only after saving in Mongo
and perform a retrieval from Mongo and transcription,
and then update the elastic
The main reason is that transcription takes time and in large databases this is significant, so I will first send the metadata and only then update the transcription




---

## Project Structure

```
summary-project-Muazzin/
├── metadata-handling/
│   ├── main.py
│   ├── manager.py
│   ├── dict_builder.py
│   └── metadata_retrieval.py
├── database-distribution/
│   ├── main.py
│   ├── manager.py
│   ├── create_unique_id.py
│   └── wav_to_binary.py
├── audio-transcription/
│   ├── main.py
│   ├── manager.py
│   ├── binary_to-wav.py
│   ├── elastic_update.py
│   └── temp_audio.wav
├── utils/
│   ├── publisher.py
│   ├── consumer.py
│   ├── class logger.py
│   └── mongo_connector.wav
├── config/
│   └── environments.py 
└── README.md
```

---

## Setup Instructions

### 1. 
```bash
```

### 2.
```bash
```

### 3.
```bash
```


---

## Project Flow

```mermaid
 
```

---

## Notes

- Right now I decided to do the transcription logic only after saving in Mongo
and perform a retrieval from Mongo and transcription,
and then update the elastic
The main reason is that transcription takes time and in large databases this is significant, so I will first send the metadata and only then update the transcription


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