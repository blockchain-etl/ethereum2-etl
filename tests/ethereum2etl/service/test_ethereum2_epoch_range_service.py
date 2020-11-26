# MIT License
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
import os

import pytest
from dateutil.parser import parse

from ethereum2etl.api.ethereum2_teku_api import Ethereum2TekuApi
from ethereum2etl.service.ethereum2_epoch_range_service import Ethereum2EpochRangeService
from ethereum2etl.service.ethereum2_service import Ethereum2Service
from tests.ethereum2etl.helpers import skip_if_slow_tests_disabled


@pytest.mark.parametrize("date,expected_start_epoch,expected_end_epoch", [
    skip_if_slow_tests_disabled(['2020-08-04', 0, 103]),
    skip_if_slow_tests_disabled(['2020-08-05', 104, 328]),
    skip_if_slow_tests_disabled(['2020-08-06', 329, 553]),
    skip_if_slow_tests_disabled(['2020-10-05', 13829, 14053]),
])
def test_get_block_range_for_date(date, expected_start_epoch, expected_end_epoch):
    ethereum2_block_range_service = get_new_ethereum2_block_range_service()
    parsed_date = parse(date)
    epochs = ethereum2_block_range_service.get_epoch_range_for_date(parsed_date)
    assert (expected_start_epoch, expected_end_epoch) == epochs


def get_new_ethereum2_block_range_service():
    return Ethereum2EpochRangeService(get_new_eth2_service())


def get_new_eth2_service():
    return Ethereum2Service(get_api())


def get_api():
    env_variable_name = "ETHEREUM2ETL_PROVIDER_URI"
    provider_uri = os.environ.get(env_variable_name)
    if provider_uri is None or len(provider_uri) == 0:
        raise ValueError('{} is required environment variable'.format(env_variable_name))

    return Ethereum2TekuApi(provider_uri)