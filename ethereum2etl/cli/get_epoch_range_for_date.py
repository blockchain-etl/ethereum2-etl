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


from datetime import datetime

import click
from blockchainetl_common.file_utils import smart_open
from blockchainetl_common.logging_utils import logging_basic_config

from ethereum2etl.service.ethereum2_epoch_range_service import Ethereum2EpochRangeService

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-d', '--date', required=True, type=lambda d: datetime.strptime(d, '%Y-%m-%d'),
              help='The date e.g. 2018-01-01.')
@click.option('-o', '--output', default='-', type=str, help='The output file. If not specified stdout is used.')
def get_epoch_range_for_date(date, output):
    ethereum2_service = Ethereum2EpochRangeService()

    start_epoch, end_epoch = ethereum2_service.get_epoch_range_for_date(date)

    with smart_open(output, 'w') as output_file:
        output_file.write('{},{}\n'.format(start_epoch, end_epoch))