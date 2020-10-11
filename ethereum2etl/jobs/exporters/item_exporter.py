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
import os
import threading

from blockchainetl_common.atomic_counter import AtomicCounter
from blockchainetl_common.exporters import JsonLinesItemExporter, CsvItemExporter
from blockchainetl_common.file_utils import get_file_handle, close_silently


class ItemExporter:
    def __init__(self, output_dir, item_type_to_filename=None, output_format='json'):
        self.output_dir = output_dir
        self.item_type_to_filename = item_type_to_filename
        if self.item_type_to_filename is None:
            self.item_type_to_filename = lambda item_type: f'{item_type}s.{output_format}'
        self.output_format = output_format
        self.exporter_mapping = {}
        self.file_mapping = {}
        self.counter_mapping = {}
        self.init_lock = threading.Lock()

        self.logger = logging.getLogger('Ethereum2ItemExporter')

    def open(self):
        pass

    def export_items(self, items):
        for item in items:
            self.export_item(item)

    def export_item(self, item):
        item_type = item.get('item_type')
        if item_type is None:
            raise ValueError('"item_type" key is not found in item {}'.format(repr(item)))

        exporter = self._get_exporter_for_item_type(item_type)
        exporter.export_item(item)

        counter = self._get_counter_for_item_type(item_type)
        counter.increment()

    def _get_exporter_for_item_type(self, item_type):
        if self.exporter_mapping.get(item_type) is None:
            with self.init_lock:
                if self.exporter_mapping.get(item_type) is None:
                    filename = os.path.join(self.output_dir, self.item_type_to_filename(item_type))
                    file = get_file_handle(filename, binary=True)
                    self.file_mapping[item_type] = file
                    self.exporter_mapping[item_type] = get_item_exporter(self.output_format, file)
        return self.exporter_mapping[item_type]

    def _get_counter_for_item_type(self, item_type):
        if self.counter_mapping.get(item_type) is None:
            with self.init_lock:
                if self.counter_mapping.get(item_type) is None:
                    self.counter_mapping[item_type] = AtomicCounter()

        return self.counter_mapping[item_type]

    def close(self):
        for item_type, file in self.file_mapping.items():
            close_silently(file)
            counter = self.counter_mapping[item_type]
            if counter is not None:
                self.logger.info('{} items exported: {}'.format(item_type, counter.increment() - 1))


def get_item_exporter(output_format, file):
    if output_format == 'json':
        return JsonLinesItemExporter(file)
    elif output_format == 'csv':
        return CsvItemExporter(file)
    else:
        ValueError(f'output format {output_format} is not recognized')
