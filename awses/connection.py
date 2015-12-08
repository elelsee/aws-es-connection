from elasticsearch import Connection
from signer import ESConnection
from urlparse import urlparse
import time

import os


class AWSConnection(Connection):

    def __init__(self, host, region, **kwargs):
        super(AWSConnection, self).__init__(host, region, **kwargs)
        self.host = host
        self.region = region
        self.token = kwargs['session_token'] if 'session_token' in kwargs else os.environ.get('AWS_SESSION_TOKEN')
        self.secret = kwargs['secret_key'] if 'secret_key' in kwargs else os.environ.get('AWS_SECRET_ACCESS_KEY')
        self.key = kwargs['access_key'] if 'access_key' in kwargs else os.environ.get('AWS_ACCESS_KEY_ID')
        self.kwargs = kwargs

    def perform_request(self, method, url, params=None,
                        body=None, timeout=None, ignore=()):
        start = time.time()
        host = urlparse(self.host).netloc.split(':')[0]
        client = ESConnection(region=self.region, 
                              host=self.host,
                              aws_access_key_id=self.key,
                              aws_secret_access_key=self.secret,
                              security_token=self.token,
                              is_secure=False)

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
