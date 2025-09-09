from elasticsearch import Elasticsearch
from config.environments import ELASTICSEARCH,INDEX_NAME

match_field = 'unique_id'
new_field = 'transcription'

class ElasticUpdate:
    def __init__(self,unique_id,transcription):
        self.es = Elasticsearch(ELASTICSEARCH)
        self.index_name = INDEX_NAME
        self.match_field = match_field
        self.value_to_match = unique_id
        self.new_field = new_field
        self.new_field_value = transcription

    def update_by_query(self):
        body = {
            "script": {
                "inline": f"if (ctx._source.{self.match_field} == params.match_value) {{ ctx._source.{self.new_field} = params.new_value; }}",
                "lang": "painless",
                "params": {
                    "match_value": self.value_to_match,
                    "new_value": self.new_field_value
                }
            },
            "query": {
                "term": {
                    self.match_field: self.value_to_match
                }
            }
        }
        response = self.es.update_by_query(index=self.index_name, body=body, conflicts="proceed")
        print(response)