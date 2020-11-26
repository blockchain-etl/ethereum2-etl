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


from ethereum2etl.domain.validator import Validator
from ethereum2etl.utils.string_utils import to_int


class ValidatorMapper(object):
    def json_dict_to_validator(self, json_dict):
        validator = Validator()

        json_dict_validator = json_dict.get('validator')

        validator.pubkey = json_dict_validator.get('pubkey')
        validator.validator_index = json_dict.get('index')
        validator.balance = to_int(json_dict.get('balance'))

        validator.withdrawal_credentials = json_dict_validator.get('withdrawal_credentials')
        validator.effective_balance = to_int(json_dict_validator.get('effective_balance'))
        validator.slashed = json_dict_validator.get('slashed')
        validator.activation_eligibility_epoch = json_dict_validator.get('activation_eligibility_epoch')
        validator.activation_epoch = json_dict_validator.get('activation_epoch')
        validator.exit_epoch = json_dict_validator.get('exit_epoch')
        validator.withdrawable_epoch = json_dict_validator.get('withdrawable_epoch')
        validator.status = json_dict.get('status')

        return validator

    def validator_to_dict(self, validator: Validator):
        return {
            **{
                'item_type': 'beacon_validator',
            },
            **vars(validator)
        }


EMPTY_OBJECT = {}


def to_binary(hex_data):
    if hex_data is None or len(hex_data) == 0:
        return hex_data

    binary = bin(int(hex_data, 16))
    # trim 0b
    if len(binary) >= 2:
        binary = binary[2:]
    return binary
