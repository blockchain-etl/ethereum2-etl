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


from ethereum2etl.domain.beacon_block import BeaconBlock
from ethereum2etl.mappers.attestation_mapper import AttestationMapper
from ethereum2etl.mappers.attester_slashing_mapper import AttesterSlashingMapper
from ethereum2etl.mappers.deposit_mapper import DepositMapper
from ethereum2etl.mappers.proposer_slashing_mapper import ProposerSlashingMapper
from ethereum2etl.mappers.voluntary_exit_mapper import VoluntaryExitMapper
from ethereum2etl.utils.string_utils import to_int
from ethereum2etl.utils.timestamp_utils import format_timestamp


class BeaconBlockMapper(object):
    def __init__(self):
        self.attestation_mapper = AttestationMapper()
        self.deposit_mapper = DepositMapper()
        self.proposer_slashing_mapper = ProposerSlashingMapper()
        self.attester_slashing_mapper = AttesterSlashingMapper()
        self.voluntary_exit_mapper = VoluntaryExitMapper()

    def json_dict_to_beacon_block(self, json_dict, timestamp, epoch):
        block = BeaconBlock()

        message = json_dict.get('data', EMPTY_OBJECT).get('message', EMPTY_OBJECT)

        slot = to_int(message.get('slot'))
        block.block_slot = to_int(slot)
        block.block_epoch = epoch
        block.block_timestamp = format_timestamp(timestamp)
        block.proposer_index = to_int(message.get('proposer_index'))

        block.block_root = json_dict.get('root')
        block.parent_root = message.get('parent_root')
        block.state_root = message.get('state_root')

        body = message.get('body')
        block.randao_reveal = body.get('randao_reveal')
        block.graffiti = body.get('graffiti')

        eth1_data = body.get('eth1_data')
        block.eth1_block_hash = eth1_data.get('block_hash')
        block.eth1_deposit_root = eth1_data.get('deposit_root')
        block.eth1_deposit_count = to_int(eth1_data.get('deposit_count'))

        block.signature = json_dict.get('beacon_block', EMPTY_OBJECT).get('signature')

        block.attestations = [self.attestation_mapper.json_dict_to_attestation(attestation)
                              for attestation in body.get('attestations', EMPTY_LIST)]

        block.deposits = [self.deposit_mapper.json_dict_to_deposit(deposit)
                              for deposit in body.get('deposits', EMPTY_LIST)]

        block.proposer_slashings = [self.proposer_slashing_mapper.json_dict_to_proposer_slashing(proposer_slashing)
                          for proposer_slashing in body.get('proposer_slashings', EMPTY_LIST)]

        block.attester_slashings = [self.attester_slashing_mapper.json_dict_to_attester_slashing(attester_slashing)
                                    for attester_slashing in body.get('attester_slashings', EMPTY_LIST)]

        block.voluntary_exits = [self.voluntary_exit_mapper.json_dict_to_voluntary_exit(voluntary_exit)
                                    for voluntary_exit in body.get('voluntary_exits', EMPTY_LIST)]

        return block

    def create_skipped_beacon_block(self, slot, timestamp, epoch):
        block = BeaconBlock()
        block.skipped = True

        block.block_slot = slot
        block.block_epoch = epoch
        block.block_timestamp = format_timestamp(timestamp)

        return block

    def beacon_block_to_dict(self, beacon_block: BeaconBlock):
        return {
            **{
                'item_type': 'beacon_block',
            },
            **vars(beacon_block),
            **{
                'attestations': [self.attestation_mapper.attestation_to_dict(a) for a in beacon_block.attestations],
                'deposits': [self.deposit_mapper.deposit_to_dict(a) for a in beacon_block.deposits],
                'proposer_slashings': [self.proposer_slashing_mapper.proposer_slashing_to_dict(p) for p in beacon_block.proposer_slashings],
                'attester_slashings': [self.attester_slashing_mapper.attester_slashing_to_dict(a) for a in beacon_block.attester_slashings],
                'voluntary_exits': [self.voluntary_exit_mapper.voluntary_exit_to_dict(v) for v in beacon_block.voluntary_exits],
            }
        }


EMPTY_OBJECT = {}
EMPTY_LIST = []
