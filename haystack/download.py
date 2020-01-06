from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=[10.10.10.115:9200]) # ELASTICSEARCH_IP is the ip of your Elasticsearch Server.
query_str = '{"query":{"range":}}'
res = es.search(index=needle, body=query_str, from_=0, size=10) # DON'T SET SIZE=100000
print(res['hits']['hits'])
