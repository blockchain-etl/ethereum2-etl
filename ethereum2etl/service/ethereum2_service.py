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

from requests import HTTPError
from ethereum2etl.utils.string_utils import to_int
from datetime import datetime


SECONDS_PER_SLOT = 12
SLOTS_PER_EPOCH = 32


class Ethereum2Service(object):
    def __init__(self, ethereum2_teku_api):
        self.ethereum2_teku_api = ethereum2_teku_api
        self.genesis_time = None

    def get_beacon_block(self, slot):
        return self.ethereum2_teku_api.get_beacon_block(slot)

    def get_beacon_validators(self):
        return self.ethereum2_teku_api.get_beacon_validators()

    def get_beacon_committees(self, epoch):
        return self.ethereum2_teku_api.get_beacon_committees(epoch=epoch)

    def get_beacon_blocks(self, slot_batch):
        if not slot_batch:
            return []

        for slot in slot_batch:
            try:
                block_response = self.get_beacon_block(slot)
                yield block_response
            except HTTPError as e:
                if e.response.status_code == 404:
                    yield None
                else:
                    raise e

    def compute_time_at_slot(self, slot):
        if slot is None:
            return None

        timestamp = self.get_genesis_time() + int(slot) * SECONDS_PER_SLOT
        return timestamp

    def compute_timestamp_at_epoch(self, epoch):
        slot = self.compute_slot_at_epoch(epoch)
        ts = self.compute_time_at_slot(slot)
        return ts

    def compute_slot_at_epoch(self, epoch):
        """
        Return the epoch number at ``slot``.
        """
        return epoch * SLOTS_PER_EPOCH

    def compute_slot_at_timestamp(self, ts):
        if ts is None:
            return None

        slot_with_fractions = self.compute_slot_with_fractions_at_timestamp(ts)
        return int(slot_with_fractions)

    def compute_slot_with_fractions_at_timestamp(self, ts):
        if ts is None:
            return None

        if isinstance(ts, datetime):
            ts = ts.timestamp()

        slot = (ts - self.get_genesis_time()) / SECONDS_PER_SLOT
        return slot

    def compute_epoch_at_timestamp(self, ts):
        slot = self.compute_slot_at_timestamp(ts)
        epoch = self.compute_epoch_at_slot(slot)
        return epoch

    def compute_epoch_at_slot(self, slot):
        """
        Return the epoch number at ``slot``.
        """
        return slot // SLOTS_PER_EPOCH

    def get_genesis_time(self):
        if self.genesis_time is None:
            genesis = self.ethereum2_teku_api.get_beacon_genesis()
            self.genesis_time = to_int(genesis['data']['genesis_time'])
        return self.genesis_time

