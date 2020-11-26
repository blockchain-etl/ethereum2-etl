# The MIT License (MIT)
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import decimal
import json

from ethereum2etl.api.request import make_get_request


class Ethereum2TekuApi:

    def __init__(self, provider_uri, timeout=300):
        self.provider_uri = provider_uri
        self.timeout = timeout

    def get_beacon_block(self, slot):
        return self.get(f'/eth/v1/beacon/blocks/{slot}')

    def get_beacon_validators(self):
        return self.get(f'/eth/v1/beacon/states/head/validators')

    def get_beacon_committees(self, epoch):
        return self.get(f'/eth/v1/beacon/states/head/committees?epoch={epoch}')

    def get_beacon_genesis(self):
        return self.get(f'/eth/v1/beacon/genesis')

    def get(self, endpoint):
        raw_response = make_get_request(
            self.provider_uri,
            endpoint,
            timeout=self.timeout
        )

        response = self._decode_api_response(raw_response)
        return response

    def _decode_api_response(self, response):
        response_text = response.decode('utf-8')
        return json.loads(response_text, parse_float=decimal.Decimal)