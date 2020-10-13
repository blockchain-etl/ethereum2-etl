## Quickstart

Install Ethereum 2.0 ETL:

```bash
pip install ethereum2-etl
```

Sync your own node or request access to node on [Infura](https://blog.infura.io/checking-your-eth-2-0-validator-balance/).

Export beacon blocks, attestations, deposits, proposer slashings, attester slashings, voluntary exits ([JSON Schema](docs/schema.md#beacon_blocksjson), 
[CSV Schema](docs/schema.md#beacon_blockscsv), 
[Reference](docs/commands.md#export_beacon_blocks)):

```bash
> ethereum2etl export_beacon_blocks --start-block 0 --end-block 200 \
--output-dir output --output-format json \
--provider-uri https://projectid:secret@medalla.infura.io
```

Export beacon validators ([JSON Schema](docs/schema.md#beacon_validatorsjson), 
[CSV Schema](docs/schema.md#beacon_validatorscsv), 
[Reference](docs/commands.md#export_beacon_validators)):

```bash
> ethereum2etl export_beacon_validtors --epoch 10 \
--output-dir output --output-format json \
--provider-uri https://projectid:secret@medalla.infura.io
```

Export beacon committees ([JSON Schema](docs/schema.md#beacon_committeesjson), 
[CSV Schema](docs/schema.md#beacon_committeescsv), 
[Reference](docs/commands.md#export_beacon_committees)):

```bash
> ethereum2etl export_beacon_committees --start-epoch 0 --end-epoch 10 \
--output-dir output --output-format json \
--provider-uri https://projectid:secret@medalla.infura.io
```

Find other commands [here](https://ethereum2-etl.readthedocs.io/en/latest/commands/).