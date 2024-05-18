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

## Supabase specific configurations

### `service_role` authorization on private schema

```sql
grant USAGE on schema my_schema to service_role;
grant all on all tables in schema my_schema to service_role;
```

### Create `trends` View

```sql
DROP VIEW IF EXISTS socialnet.trends;
CREATE VIEW socialnet.trends AS
SELECT
    name,
    COUNT(*) AS count,
    ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS position
FROM     socialnet."Hashtags"
WHERE    created_at >= Now() - interval '1 DAYS'
group BY name
ORDER BY count DESC limit 10;
```