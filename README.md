# Ethereum 2.0 ETL


For the latest version, check out the repo and call 
```bash
> pip install -e . 
> python ethereum2etl.py
```

## Running Tests

```bash
pip install -e .[dev]
echo "ETHEREUM2ETL_PROVIDER_URI variable is optional"
export ETHEREUM2SETL_PROVIDER_URI=https://projectid:secret@medalla.infura.io
pytest -vv
```