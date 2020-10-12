# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
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


from ethereum2etl.domain.committee import Committee
from ethereum2etl.utils.ethereum2_utils import compute_timestamp_at_epoch
from ethereum2etl.utils.string_utils import to_int
from ethereum2etl.utils.timestamp_utils import format_timestamp


class CommitteeMapper(object):
    def json_dict_to_committee(self, json_dict, epoch):
        committee = Committee()

        committee.epoch = epoch
        committee.epoch_timestamp = format_timestamp(compute_timestamp_at_epoch(epoch))
        committee.slot = to_int(json_dict.get('slot'))
        committee.index = to_int(json_dict.get('index'))
        committee.committee = json_dict.get('committee')

        return committee

    def committee_to_dict(self, committee: Committee):
        return {
            **{
                'item_type': 'beacon_committee',
            },
            **vars(committee)
        }


EMPTY_OBJECT = {}
