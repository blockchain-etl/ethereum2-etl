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


from ethereum2etl.domain.attestation import Attestation
from ethereum2etl.utils.string_utils import to_int


class AttestationMapper(object):

    def json_dict_to_attestation(self, json_dict):
        attestation = Attestation()

        attestation.aggregation_bits = hex_to_aggregation_bits(json_dict.get('aggregation_bits'))

        data = json_dict.get('data', EMPTY_OBJECT)
        attestation.slot = to_int(data.get('slot'))
        attestation.index = to_int(data.get('index'))
        attestation.beacon_block_root = data.get('beacon_block_root')

        attestation.source_epoch = to_int(data.get('source', EMPTY_OBJECT).get('epoch'))
        attestation.source_root = data.get('source', EMPTY_OBJECT).get('root')
        attestation.target_epoch = to_int(data.get('target', EMPTY_OBJECT).get('epoch'))
        attestation.target_root = data.get('target', EMPTY_OBJECT).get('root')

        attestation.signature = json_dict.get('signature')

        return attestation

    def attestation_to_dict(self, attestation: Attestation):
        return {
            **{
                'item_type': 'attestation',
            },
            **vars(attestation)
        }


EMPTY_OBJECT = {}


def hex_to_aggregation_bits(hex_aggregation_bits):
    aggregation_bits = to_binary(hex_aggregation_bits)
    if len(aggregation_bits) >= 1:
        # The first set bit indicates the start of aggregation bits
        # The binary string returned by to_binary() always starts with 1
        aggregation_bits = aggregation_bits[1:]
    return aggregation_bits


def to_binary(hex_data):
    if hex_data is None or len(hex_data) == 0:
        return hex_data

    if hex_data.startswith('0x'):
        hex_data = hex_data[2:]

    b = bytearray.fromhex(hex_data)

    binary = bin(int.from_bytes(b, byteorder='little'))

    if binary is not None and binary.startswith('0b'):
        binary = binary[2:]
    return binary
