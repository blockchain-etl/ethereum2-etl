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


from ethereum2etl.domain.attester_slashing import AttesterSlashing
from ethereum2etl.utils.string_utils import to_int


class AttesterSlashingMapper(object):

    def json_dict_to_attester_slashing(self, json_dict):
        attester_slashing = AttesterSlashing()

        attestation1 = json_dict.get('attestation_1', EMPTY_OBJECT)
        attestation1_data = attestation1.get('data', EMPTY_OBJECT)

        attestation2 = json_dict.get('attestation_2', EMPTY_OBJECT)
        attestation2_data = attestation2.get('data', EMPTY_OBJECT)

        attester_slashing.attestation_1_attesting_indices = attestation1.get('attesting_indices')
        attester_slashing.attestation_1_slot = to_int(attestation1_data.get('slot'))
        attester_slashing.attestation_1_index = to_int(attestation1_data.get('index'))
        attester_slashing.attestation_1_beacon_block_root = attestation1_data.get('beacon_block_root')
        attester_slashing.attestation_1_source_epoch = to_int(attestation1_data.get('source').get('epoch'))
        attester_slashing.attestation_1_source_root = attestation1_data.get('source').get('root')
        attester_slashing.attestation_1_target_epoch = to_int(attestation1_data.get('target').get('epoch'))
        attester_slashing.attestation_1_target_root = attestation1_data.get('target').get('root')
        attester_slashing.attestation_1_signature = attestation1.get('signature')

        attester_slashing.attestation_2_attesting_indices = attestation2.get('attesting_indices')
        attester_slashing.attestation_2_slot = to_int(attestation2_data.get('slot'))
        attester_slashing.attestation_2_index = to_int(attestation2_data.get('index'))
        attester_slashing.attestation_2_beacon_block_root = attestation2_data.get('beacon_block_root')
        attester_slashing.attestation_2_source_epoch = to_int(attestation2_data.get('source').get('epoch'))
        attester_slashing.attestation_2_source_root = attestation2_data.get('source').get('root')
        attester_slashing.attestation_2_target_epoch = to_int(attestation2_data.get('target').get('epoch'))
        attester_slashing.attestation_2_target_root = attestation2_data.get('target').get('root')
        attester_slashing.attestation_2_signature = attestation2.get('signature')

        return attester_slashing

    def attester_slashing_to_dict(self, attester_slashing: AttesterSlashing):
        return {
            **{
                'item_type': 'attester_slashing',
            },
            **vars(attester_slashing)
        }


EMPTY_OBJECT = {}
