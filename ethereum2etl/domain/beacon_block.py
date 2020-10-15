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


class BeaconBlock(object):
    def __init__(self):
        self.block_slot = None
        self.block_epoch = None
        self.block_timestamp = None
        self.proposer_index = None

        self.skipped = False

        self.block_root = None
        self.parent_root = None
        self.state_root = None

        self.randao_reveal = None
        self.graffiti = None

        self.eth1_block_hash = None
        self.eth1_deposit_root = None
        self.eth1_deposit_count = None

        self.signature = None

        self.attestations = []
        self.deposits = []
        self.proposer_slashings = []
        self.attester_slashings = []
        self.voluntary_exits = []
