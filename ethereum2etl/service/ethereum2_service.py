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


class Ethereum2Service(object):
    def __init__(self, ethereum2_teku_api):
        self.ethereum2_teku_api = ethereum2_teku_api

    def get_beacon_block(self, slot):
        return self.ethereum2_teku_api.get_beacon_block(slot)

    def get_beacon_validators(self, epoch, page_number, page_size=100):
        return self.ethereum2_teku_api.get_beacon_validators(epoch=epoch, page_token=page_number, page_size=page_size)

    def get_beacon_committees(self, epoch):
        return self.ethereum2_teku_api.get_beacon_committees(epoch=epoch)

    def get_beacon_blocks(self, slot_batch):
        if not slot_batch:
            return []

        for slot in slot_batch:
            block_response = self.get_beacon_block(slot)
            returned_slot = block_response.get('beacon_block').get('message').get('slot')
            # Teku returns latest non-skipped block
            if returned_slot is None or int(returned_slot) != slot:
                yield None
            else:
                yield block_response
