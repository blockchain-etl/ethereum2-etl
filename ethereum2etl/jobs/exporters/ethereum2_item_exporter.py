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

from ethereum2etl.jobs.exporters.item_exporter import ItemExporter


class Ethereum2ItemExporter:
    def __init__(self, output_dir, item_type_to_filename=None, output_format='json'):
        self.delegate = ItemExporter(output_dir, item_type_to_filename, output_format)
        self.output_format = output_format

    def open(self):
        self.delegate.open()

    def export_items(self, items):
        for item in items:
            self.export_item(item)

    def export_item(self, item):
        item_type = item.get('item_type')
        if item_type is None:
            raise ValueError('"item_type" key is not found in item {}'.format(repr(item)))

        if self.output_format == 'csv' and item_type == 'beacon_block':
            extra_fields = {
                'block_slot': item.get('block_slot'),
                'block_timestamp': item.get('block_timestamp'),
            }
            self._export_nested_items(item, 'attestations', extra_fields)
            self._export_nested_items(item, 'deposits', extra_fields)
            self._export_nested_items(item, 'proposer_slashings', extra_fields)
            self._export_nested_items(item, 'attester_slashings', extra_fields)
            self._export_nested_items(item, 'voluntary_exits', extra_fields)

            self.delegate.export_item(item)
        else:
            self.delegate.export_item(item)

    def _export_nested_items(self, item, nested_items_key, extra_fields):
        for nested_item in item.get(nested_items_key, EMPTY_LIST):
            if extra_fields is not None:
                nested_item = {
                    **nested_item,
                    **extra_fields,
                }
            self.delegate.export_item(nested_item)
        del item[nested_items_key]

    def close(self):
        self.delegate.close()


EMPTY_LIST = []
