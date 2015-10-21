from elasticsearch import Connection
from es_signer import ESConnection
from urlparse import urlparse


class AWSConnection(Connection):

    def __init__(self, host=None, region=None, **kwargs):
        super(AWSConnection, self).__init__(host=host,
                                            region=region,
                                            **kwargs)
        self.region = region

    def perform_request(self, method, url, params=None,
                        body=None, timeout=None, ignore=()):
        host = urlparse(self.host).netloc.split(':')[0]
        client = ESConnection(region=self.region, host=host)
        response = client.make_request(method, path=url, params=params)
        raw_data = response.read().decode('utf-8')
        return response.status, dict(response.getheaders()), raw_data
