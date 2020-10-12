# Commands

All the commands accept `-h` parameter for help, e.g.:

```bash
> ethereum2etl export_beacon_blocks -h

Usage: ethereum2etl export_beacon_blocks [OPTIONS]

Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote Ethereum 2 node
                                  [default: https://medalla.infura.io]
  -r, --rate-limit INTEGER        Maximum requests per second for provider in
                                  case it has rate limiting
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json|csv]  The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

#### export_beacon_blocks

```bash
> ethereum2etl export_beacon_blocks --start-block 0 --end-block 1000 \
--provider-uri https://projectid:secret@medalla.infura.io \
--output-dir output --output-format json
```

Usage:

```bash
Usage: ethereum2etl export_beacon_blocks [OPTIONS]

Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote Ethereum 2 node
                                  [default: https://medalla.infura.io]
  -r, --rate-limit INTEGER        Maximum requests per second for provider in
                                  case it has rate limiting
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json|csv]  The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

If `--output-format` is `json` output will be in [beacon_blocks.json](schema.md#beacon_blocksjson).

If `--output-format` is `csv` output will be in [beacon_blocks.csv](schema.md#beacon_blockscsv), nested data structures 
will be output to 
`attestations.csv`, 
`deposits.csv`, 
`proposer_slashings.csv`,
`attester_slashings.csv`, 
`voluntary_exits.csv`. 

#### export_beacon_validators

```bash
> ethereum2etl export_beacon_validators --epoch 0 \
--provider-uri https://projectid:secret@medalla.infura.io \
--output-dir output --output-format json
```

Usage:

```bash
Usage: ethereum2etl export_beacon_validators [OPTIONS]

Options:
  -e, --epoch INTEGER             Epoch number, if not provided latest epoch
                                  number is used.
  -p, --provider-uri TEXT         The URI of the remote Ethereum 2 node
                                  [default: https://medalla.infura.io]
  -r, --rate-limit INTEGER        Maximum requests per second for provider in
                                  case it has rate limiting
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json|csv]  The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

Output to [beacon_validators.json](schema.md#beacon_validatorsjson) or [beacon_validators.csv](schema.md#beacon_validatorscsv).

#### export_beacon_committees

```bash
> ethereum2etl export_beacon_committees --start-epoch 0 --end-epoch 10 \
--provider-uri https://projectid:secret@medalla.infura.io \
--output-dir output --output-format json
```

Usage:

```bash
Usage: ethereum2etl export_beacon_committees [OPTIONS]

Options:
  -s, --start-epoch INTEGER       Start epoch  [default: 0]
  -e, --end-epoch INTEGER         End epoch  [required]
  -p, --provider-uri TEXT         The URI of the remote Ethereum 2 node
                                  [default: https://medalla.infura.io]
  -r, --rate-limit INTEGER        Maximum requests per second for provider in
                                  case it has rate limiting
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json|csv]  The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

Output to [beacon_committees.json](schema.md#beacon_committeesjson) or [beacon_committees.csv](schema.md#beacon_committeescsv).

#### get_block_range_for_date

```bash
> ethereum2etl get_block_range_for_date --date 2020-08-04
0,3299
```

Usage:

```bash
Usage: ethereum2etl get_block_range_for_date [OPTIONS]

  Outputs start and end blocks for a given date.

Options:
  -d, --date <LAMBDA>  The date e.g. 2018-01-01.  [required]
  -o, --output TEXT    The output file. If not specified stdout is used.
  -h, --help           Show this message and exit.
```