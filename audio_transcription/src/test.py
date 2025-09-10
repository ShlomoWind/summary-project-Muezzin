# from elasticsearch import Elasticsearch
#
# class ElasticsearchUpdater:
#     def __init__(self):
#         self.es = Elasticsearch("http://localhost:9200")
#
#     def update_document_by_field(self, field_to_match, value_to_match, new_fields_and_values):
#         script_parts = []
#         for field, value in new_fields_and_values.items():
#             script_parts.append(f"ctx._source.{field} = params.{field}")
#         script_code = "; ".join(script_parts)
#         body = {
#             "query": {
#                 "match": {
#                     field_to_match: value_to_match
#                 }
#             },
#             "script": {
#                 "source": script_code,
#                 "lang": "painless",
#                 "params": new_fields_and_values
#             }
#         }
#
#         try:
#             response = self.es.update_by_query(
#                 index="my_3_test",
#                 body=body,
#                 conflicts='proceed'
#             )
#             print(f"Update by query response: {response}")
#             return response
#         except Exception as e:
#             print(f"Error updating documents: {e}")
#             return None
#
# # Example Usage:
# if __name__ == "__main__":
#     updater = ElasticsearchUpdater()
#
#     # Example: Update documents where 'product_id' is 'P123'
#     # Add/update 'last_updated' and 'status' fields
#     new_data = {
#         "sssssssssssssssssssssss": "2025-09-10T12:00:00Z",
#         "status": "processed",
#         "new_feature": "enabled"
#     }
#     updater.update_document_by_field("unique_id", "a462fa6f32e06cf7048cbd108e2805dc927b2d55d1e45f437ccf0625258c0e7e", new_data)
#
#     # Example: Update documents where 'category' is 'electronics'
#     # Add/update 'discount_percentage'
#     new_data_2 = {
#         "discount_percentage": 15
#     }
#     updater.update_document_by_field("unique_id", "a462fa6f32e06cf7048cbd108e2805dc927b2d55d1e45f437ccf0625258c0e7e", new_data_2)