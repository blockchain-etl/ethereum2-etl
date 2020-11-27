# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
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


import os

import pytest

from ethereum2etl.api.ethereum2_teku_api import Ethereum2TekuApi
from ethereum2etl.service.ethereum2_service import Ethereum2Service


def run_slow_tests():
    provider_uri_variable = os.environ.get('ETHEREUM2ETL_PROVIDER_URI', '')
    return provider_uri_variable is not None and len(provider_uri_variable) > 0


def skip_if_slow_tests_disabled(data):
    return pytest.param(*data, marks=pytest.mark.skipif(not run_slow_tests(),
                                                        reason='Skipping slow running tests'))


def get_new_eth2_service():
    return Ethereum2Service(get_api())


def get_api():
    env_variable_name = "ETHEREUM2ETL_PROVIDER_URI"
    provider_uri = os.environ.get(env_variable_name)
    if provider_uri is None or len(provider_uri) == 0:
        raise ValueError('{} is required environment variable'.format(env_variable_name))

    return Ethereum2TekuApi(provider_uri)