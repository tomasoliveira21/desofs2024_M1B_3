# Backend for SocialNet

## How to use

1. Install [`pyenv`](https://github.com/pyenv/pyenv):

```shell
curl https://pyenv.run | bash
```

2. Install Python 3.12:

```shell
pyenv install 3.12
```


3. Install [`poetry`]():

```shell
pip install poetry
```

4. Initiate a virtual environment:

```shell
python -m venv .venv
```

5. Install Packages:

```shell
poetry install
```

6. Launch the application:

```shell
poetry shell
uvicorn backend.main:app --reload --port 5000
```

## PGAdmin

For M1 Macs:
 
```shell
$ docker run -p 8000:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=desofs@isep.ipp.pt' \
    -e 'PGADMIN_DEFAULT_PASSWORD=desofs' \
    -d --platform linux/amd64 dpage/pgadmin4
```