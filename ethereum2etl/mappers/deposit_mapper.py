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


from ethereum2etl.domain.deposit import Deposit
from ethereum2etl.utils.string_utils import to_int


class DepositMapper(object):

    def json_dict_to_deposit(self, json_dict):
        deposit = Deposit()

        data = json_dict.get('data', EMPTY_OBJECT)

        deposit.pubkey = data.get('pubkey')
        deposit.withdrawal_credentials = data.get('withdrawal_credentials')
        deposit.amount = to_int(data.get('amount'))
        deposit.signature = data.get('signature')

        return deposit

    def deposit_to_dict(self, deposit: Deposit):
        return {
            **{
                'item_type': 'deposit',
            },
            **vars(deposit)
        }


EMPTY_OBJECT = {}
