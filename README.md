## Setup

Ensure you have
[pipenv already installed](https://automationhacks.io/2020/07/12/how-to-manage-your-python-virtualenvs-with-pipenv/):

```zsh
# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install
```



Note: These are the marks ou can use to run the test
```zsh
login
customers
cards
orders
catalogue
register
```

## How to run

```zsh
# Setup report portal on docker
# Update rp_uuid in pytest.ini with project token
docker-compose -p reportportal up -d --force-recreate

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run specific module
python -m pytest -v -m [marks]

# Run tests in parallel
python -m pytest -n auto

# Report results to report portal
python -m pytest -n auto --reportportal
```
