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

import click

from ethereum2etl.cli.export_beacon_committees import export_beacon_committees
from ethereum2etl.cli.export_beacon_validators import export_beacon_validators
from ethereum2etl.cli.export_beacon_blocks import export_beacon_blocks
from ethereum2etl.cli.get_block_range_for_date import get_block_range_for_date
from ethereum2etl.cli.get_epoch_range_for_date import get_epoch_range_for_date


@click.group()
@click.version_option(version='0.0.7')
@click.pass_context
def cli(ctx):
    pass


# export
cli.add_command(export_beacon_blocks, "export_beacon_blocks")
cli.add_command(export_beacon_validators, "export_beacon_validators")
cli.add_command(export_beacon_committees, "export_beacon_committees")

# utils
cli.add_command(get_block_range_for_date, "get_block_range_for_date")
cli.add_command(get_epoch_range_for_date, "get_epoch_range_for_date")
