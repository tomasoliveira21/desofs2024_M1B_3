import os
import secrets

import dotenv
import pytest
import supabase
from fastapi.testclient import TestClient

from backend.main import app

dotenv.load_dotenv()

expired_jwt = os.environ.get("TEST_EXPIRED_JWT", "")


@pytest.fixture()
def supabase_setup():
    client = supabase.create_client(
        supabase_url=os.environ.get("SUPABASE_URL", ""),
        supabase_key=os.environ.get(
            "SUPABASE_KEY",
            "",
        ),
    )
    client.auth.sign_in_with_password(
        credentials={
            "email": os.environ.get("TEST_USER_EMAIL", ""),
            "password": os.environ.get("TEST_USER_PASSWORD", ""),
        }
    )
    yield client
    client.auth.sign_out()


def test_get_tweets_no_auth():
    with TestClient(app) as client:
        response = client.get("/tweet/all")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }
    client.close()


def test_get_tweets_valid_auth(supabase_setup):
    with TestClient(app) as client:
        response = client.get(
            "/tweet/all",
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 200
        assert response.json() is not None
    client.close()


def test_get_tweets_expired_auth():
    with TestClient(app) as client:
        response = client.get(
            "/tweet/all", headers={"Authorization": f"Bearer {expired_jwt}"}
        )
        assert response.status_code == 500
        assert response.json() == {"detail": "Could not decode JWT Token."}
    client.close()


def test_post_tweet_no_auth():
    with TestClient(app) as client:
        response = client.post(
            "/tweet",
            json={"content": "whatever"},
        )
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }
    client.close()


def test_post_delete_tweet_valid_auth(supabase_setup):
    with TestClient(app) as client:
        response = client.post(
            "/tweet",
            json={
                "content": "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstri"
            },
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 200
        id = response.json()["uuid"]
        response = client.delete(
            "/tweet",
            params={"uuid": id},
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 200
    client.close()


def test_post_tweet_bigger_than(supabase_setup):
    with TestClient(app) as client:
        random_string = secrets.token_hex(1201)[:-1]
        response = client.post(
            "/tweet",
            json={"content": random_string},
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 422
    client.close()


def test_post_tweet_smaller_than(supabase_setup):
    with TestClient(app) as client:
        random_string = ""
        response = client.post(
            "/tweet",
            json={"content": random_string},
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 422
    client.close()


def test_get_hashtags_no_auth():
    with TestClient(app) as client:
        response = client.get("/hashtag")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }
    client.close()


def test_get_hashtags_valid_auth(supabase_setup):
    with TestClient(app) as client:
        response = client.get(
            "/hashtag",
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 200
        assert response.json() is not None
    client.close()


def test_get_trends_no_auth():
    with TestClient(app) as client:
        response = client.get("/hashtag/trends")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }
    client.close()


def test_get_trends_valid_auth(supabase_setup):
    with TestClient(app, raise_server_exceptions=True) as client:
        response = client.get(
            "/hashtag/trends",
            headers={
                "Authorization": f"Bearer {supabase_setup.auth.get_session().access_token}"
            },
        )
        assert response.status_code == 200
        assert response.json() is not None
    client.close()
