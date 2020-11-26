# Ethereum 2.0 ETL

[![Build Status](https://travis-ci.org/blockchain-etl/ethereum2-etl.png)](https://travis-ci.org/blockchain-etl/ethereum2-etl)
[![Join the chat at https://gitter.im/ethereum-eth](https://badges.gitter.im/ethereum-etl.svg)](https://gitter.im/ethereum-etl/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Telegram](https://img.shields.io/badge/telegram-join%20chat-blue.svg)](https://t.me/joinchat/GsMpbA3mv1OJ6YMp3T5ORQ)
[![Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/wukrezR)

Ethereum 2.0 ETL lets you convert blockchain data into convenient formats like CSVs and relational databases.

*Do you just want to query Ethereum data right away? Use the [public dataset in BigQuery](https://console.cloud.google.com/bigquery?page=dataset&d=crypto_ethereum2_medalla&p=public-data-finance).*

[Full documentation available here](http://ethereum2-etl.readthedocs.io/).

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
Read [this article](https://research.nansen.ai/ethereum-2-0-etl-and-medalla-data-in-google-bigquery/) for 
example SQL queries.

For the latest version, check out the repo and call 
```bash
> pip install -e . 
> python ethereum2etl.py
```

## Useful Links

- [Schema](https://ethereum2-etl.readthedocs.io/en/latest/schema/)
- [Command Reference](https://ethereum2-etl.readthedocs.io/en/latest/commands/)
- [Documentation](https://ethereum2-etl.readthedocs.io/)
- [Airflow DAGs](https://github.com/blockchain-etl/ethereum2-etl-airflow)

## Running Tests

```bash
> pip install -e .[dev]
> export ETHEREUM2ETL_PROVIDER_URI=https://projectid:secret@medalla.infura.io
> pytest -vv
```

### Running Tox Tests

```bash
> pip install tox
> tox
```

## Running in Docker

1. Install Docker https://docs.docker.com/install/

2. Build a docker image
        
        > docker build -t ethereum2-etl:latest .
        > docker image ls
        
3. Run a container out of the image

        > docker run -v $HOME/output:/ethereum2-etl/output ethereum2-etl:latest export_beacon_blocks -s 0 -e 200 -p https://projectid:secret@medalla.infura.io
        > docker run -v $HOME/output:/ethereum2-etl/output ethereum2-etl:latest export_beacon_blocks -s 2020-08-04 -e 2020-08-05 -p https://projectid:secret@medalla.infura.io


## Projects using Ethereum ETL

* [Google](https://goo.gl/oY5BCQ) - Public BigQuery Ethereum datasets
* [Nansen](https://nansen.ai/?ref=ethereum2etl) - Blockchain analytics platform
* [Medalla Data Challenge](https://blog.ethereum.org/2020/11/17/medalla-data-challenge-results/) - analyses of the Ethereum 2.0 blockchain
