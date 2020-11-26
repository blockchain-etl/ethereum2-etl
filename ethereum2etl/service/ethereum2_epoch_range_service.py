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

from datetime import datetime, timezone

from blockchainetl_common.graph.graph_operations import OutOfBoundsError


class Ethereum2EpochRangeService(object):

    def __init__(self, ethereum2_service):
        self.ethereum2_service = ethereum2_service

    def get_epoch_range_for_date(self, date):
        start_datetime = datetime.combine(date, datetime.min.time().replace(tzinfo=timezone.utc))
        end_datetime = datetime.combine(date, datetime.max.time().replace(tzinfo=timezone.utc))
        return self.get_epoch_range_for_timestamps(start_datetime.timestamp(), end_datetime.timestamp())

    def get_epoch_range_for_timestamps(self, start_timestamp, end_timestamp):
        start_timestamp = int(start_timestamp)
        end_timestamp = int(end_timestamp)
        if start_timestamp > end_timestamp:
            raise ValueError('start_timestamp must be greater or equal to end_timestamp')

        start_epoch = self.ethereum2_service.compute_epoch_at_timestamp(start_timestamp)
        end_epoch = self.ethereum2_service.compute_epoch_at_timestamp(end_timestamp)

        if start_epoch < 0 and end_epoch < 0:
            raise OutOfBoundsError('The given timestamp range does not cover any epochs')

        if start_epoch < 0:
            start_epoch = 0

        if end_epoch < 0:
            end_epoch = 0

        timestamp_at_epoch = self.ethereum2_service.compute_timestamp_at_epoch(start_epoch)
        if timestamp_at_epoch < start_timestamp:
            start_epoch += 1

        return start_epoch, end_epoch


