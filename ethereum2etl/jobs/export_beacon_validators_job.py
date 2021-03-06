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

import logging

from blockchainetl_common.executors.batch_work_executor import BatchWorkExecutor
from blockchainetl_common.jobs.base_job import BaseJob

from ethereum2etl.mappers.validator_mapper import ValidatorMapper


class ExportBeaconValidatorsJob(BaseJob):
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

        self.batch_size=batch_size
        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter

        self.ethereum2_service = ethereum2_service

        self.validator_mapper = ValidatorMapper()

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
        slot = self.ethereum2_service.compute_slot_at_epoch(epoch)
        logging.info(f'Slot for epoch {epoch} is {slot}')
        validators_response = self.ethereum2_service.get_beacon_validators(slot)

        timestamp = self.ethereum2_service.compute_time_at_slot(slot)

        for validator_response in validators_response['data']:
            validator = self.validator_mapper.json_dict_to_validator(validator_response, timestamp, epoch)
            self.item_exporter.export_item(self.validator_mapper.validator_to_dict(validator))

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()
