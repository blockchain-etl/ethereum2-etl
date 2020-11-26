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

from blockchainetl_common.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl_common.jobs.base_job import BaseJob
from blockchainetl_common.utils import validate_range

from ethereum2etl.mappers.beacon_block_mapper import BeaconBlockMapper


class ExportBeaconBlocksJob(BaseJob):
    def __init__(
            self,
            start_block,
            end_block,
            ethereum2_service,
            max_workers,
            item_exporter,
            batch_size=1):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter

        self.ethereum2_service = ethereum2_service

        self.beacon_block_mapper = BeaconBlockMapper()

    def _start(self):
        self.item_exporter.open()

    def _export(self):
        self.batch_work_executor.execute(
            range(self.start_block, self.end_block + 1),
            self._export_batch,
            total_items=self.end_block - self.start_block + 1
        )

    def _export_batch(self, slot_batch):
        responses = list(self.ethereum2_service.get_beacon_blocks(slot_batch))
        assert len(slot_batch) == len(responses)
        for slot, response in zip(slot_batch, responses):
            timestamp = self.ethereum2_service.compute_time_at_slot(slot)
            epoch = self.ethereum2_service.compute_epoch_at_slot(slot)
            if response is not None:
                beacon_block = self.beacon_block_mapper.json_dict_to_beacon_block(response, timestamp, epoch)
            else:
                beacon_block = self.beacon_block_mapper.create_skipped_beacon_block(slot, timestamp, epoch)

            self.item_exporter.export_item(self.beacon_block_mapper.beacon_block_to_dict(beacon_block))

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()
