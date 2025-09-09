# summary-project-Muezzin

Right now I decided to do the transcription logic only after saving in Mongo
and perform a retrieval from Mongo and transcription,
and then update the elastic
The main reason is that transcription takes time and in large databases this is significant, so I will first send the metadata and only then update the transcription