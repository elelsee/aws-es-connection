from elasticsearch import Connection
from signer import ESConnection
from urlparse import urlparse
import time


class AWSConnection(Connection):

    def __init__(self, host=None, region=None, **kwargs):
        super(AWSConnection, self).__init__(host=host,
                                            region=region,
                                            **kwargs)
        self.region = region

    def perform_request(self, method, url, params=None,
                        body=None, timeout=None, ignore=()):
        start = time.time()
        host = urlparse(self.host).netloc.split(':')[0]
        client = ESConnection(region=self.region, host=host)

        if body:
            response = client.make_request(method, path=url, params=params, data=body)
        else:
            response = client.make_request(method, path=url, params=params)

        duration = time.time() - start
        raw_data = response.read().decode('utf-8')

        if not (200 <= response.status < 300) and response.status not in ignore:
            self.log_request_fail(method, host, body, duration, response.status)
            self._raise_error(response.status, raw_data)

        return response.status, dict(response.getheaders()), raw_data
