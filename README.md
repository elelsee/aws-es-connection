# aws-es-connection
[Python Elasticsearch Client](https://github.com/elastic/elasticsearch-py) Connection Class for AWS Elasticsearch Service

Usage:
``` python
from awses.connection import AWSConnection
from elasticsearch import Elasticsearch

es = Elasticsearch(connection_class=AWSConnection,
                   region='us-east-1',
                   host='search-domain-b4tn7dis4q2epw6g37akda6nh4.us-east-1.es.amazonaws.com')

es.search()
{u'_shards': {u'failed': 0, u'successful': 5, u'total': 5},
 u'hits': {u'hits': [], u'max_score': None, u'total': 0},
 u'timed_out': False,
 u'took': 1}

es.info()
{u'cluster_name': u'620726645985:domain',
 u'name': u'Bloodlust',
 u'status': 200,
 u'tagline': u'You Know, for Search',
 u'version': {u'build_hash': u'62ff9868b4c8a0c45860bebb259e21980778ab1c',
  u'build_snapshot': False,
  u'build_timestamp': u'2015-04-27T09:21:06Z',
  u'lucene_version': u'4.10.4',
  u'number': u'1.5.2'}}
  ```
