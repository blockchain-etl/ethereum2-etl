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

import time

from blockchainetl_common.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl_common.jobs.base_job import BaseJob

from ethereum2etl.mappers.committee_mapper import CommitteeMapper


class ExportBeaconCommitteesJob(BaseJob):
    def __init__(
            self,
            start_epoch,
            end_epoch,
            ethereum2_service,
            max_workers,
            item_exporter,
            batch_size=1):
        self.start_epoch = start_epoch
        self.end_epoch = end_epoch

        self.batch_size = batch_size
        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter

        self.ethereum2_service = ethereum2_service

        self.committee_mapper = CommitteeMapper()

    def _start(self):
        self.item_exporter.open()

    def _export(self):
        self.batch_work_executor.execute(
            range(self.start_epoch, self.end_epoch + 1),
            self._export_batch,
            total_items=self.end_epoch - self.start_epoch + 1
        )

    def _export_batch(self, epoch_batch):
        for epoch in epoch_batch:
            self._export_epoch(epoch)

    def _export_epoch(self, epoch):
        committees_response = self.ethereum2_service.get_beacon_committees(epoch)
        data = committees_response['data']

        for committee_response in data:
            timestamp = self.ethereum2_service.compute_timestamp_at_epoch(epoch)
            committee = self.committee_mapper.json_dict_to_committee(committee_response, epoch=epoch, timestamp=timestamp)
            self.item_exporter.export_item(self.committee_mapper.committee_to_dict(committee))

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()
