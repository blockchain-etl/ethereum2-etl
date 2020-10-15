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


from ethereum2etl.domain.proposer_slashing import ProposerSlashing
from ethereum2etl.utils.string_utils import to_int


class ProposerSlashingMapper(object):

    def json_dict_to_proposer_slashing(self, json_dict):
        proposer_slashing = ProposerSlashing()

        header1 = json_dict.get('header_1', EMPTY_OBJECT)
        header1_message = header1.get('message', EMPTY_OBJECT)

        header2 = json_dict.get('header_2', EMPTY_OBJECT)
        header2_message = header2.get('message', EMPTY_OBJECT)

        proposer_slashing.header_1_slot = to_int(header1_message.get('slot'))
        proposer_slashing.header_1_proposer_index = to_int(header1_message.get('proposer_index'))
        proposer_slashing.header_1_parent_root = header1_message.get('parent_root')
        proposer_slashing.header_1_state_root = header1_message.get('state_root')
        proposer_slashing.header_1_body_root = header1_message.get('body_root')
        proposer_slashing.header_1_signature = header1.get('signature')

        proposer_slashing.header_2_slot = to_int(header2_message.get('slot'))
        proposer_slashing.header_2_proposer_index = to_int(header2_message.get('proposer_index'))
        proposer_slashing.header_2_parent_root = header2_message.get('parent_root')
        proposer_slashing.header_2_state_root = header2_message.get('state_root')
        proposer_slashing.header_2_body_root = header2_message.get('body_root')
        proposer_slashing.header_2_signature = header2.get('signature')

        return proposer_slashing

    def proposer_slashing_to_dict(self, proposer_slashing: ProposerSlashing):
        return {
            **{
                'item_type': 'proposer_slashing',
            },
            **vars(proposer_slashing)
        }


EMPTY_OBJECT = {}
