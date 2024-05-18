import os
import secrets

from fastapi.testclient import TestClient
from gotrue.types import SignInWithPasswordCredentials

import supabase
from backend.main import app

expired_jwt = "eyJhbGciOiJIUzI1NiIsImtpZCI6Im4vWWpIdEc4dVk4OU9OQkgiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE1OTc1MzIwLCJpYXQiOjE3MTU5NzE3MjAsImlzcyI6Imh0dHBzOi8vbnpucGJrbG9xdmtlbnhiY3B0anUuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjU5Y2JlYjA1LWIzZTMtNDAyNy04MWQ5LTFiNWU2ZDkwNGM2YiIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7fSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTcxNTk3MTcyMH1dLCJzZXNzaW9uX2lkIjoiN2FmZDVjMzItOTAxMC00N2UwLTlmYTUtYzliMTkxNDRjNTgxIiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.IwKaCaJUHIX80ZTUMczif0c44elvLPe1IMsGZ225MJg"

test_user: SignInWithPasswordCredentials = {
    "email": os.environ.get("TEST_USER_EMAIL", "desofs-test@isep.ipp.pt"),
    "password": os.environ.get("TEST_USER_PASSWORD", "7jTdM&^hdy74rWbH"),
}


def sign_in_with_password(test_user: SignInWithPasswordCredentials):
    client = supabase.create_client(
        supabase_url=os.environ.get(
            "SUPABASE_AUTH_URL", "https://nznpbkloqvkenxbcptju.supabase.co"
        ),
        supabase_key=os.environ.get(
            "SUPABASE_AUTH_KEY",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im56bnBia2xvcXZrZW54YmNwdGp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUxMDU4OTQsImV4cCI6MjAzMDY4MTg5NH0.8ndlKplM6WwJfdEG_UhlHxbGCaz_q2NDcMQA-cMxoyQ",
        ),
    )
    data = client.auth.sign_in_with_password(test_user)
    return data, client


def test_get_tweets_no_auth():
    with TestClient(app) as client:
        response = client.get("/tweet")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }


def test_get_tweets_valid_auth():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        response = client.get(
            "/tweet",
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 200
        assert response.json() is not None
    supabase[1].auth.sign_out()


def test_get_tweets_expired_auth():
    with TestClient(app) as client:
        response = client.get(
            "/tweet", headers={"Authorization": f"Bearer {expired_jwt}"}
        )
        assert response.status_code == 403
        assert response.json() == {"detail": "Invalid token or expired token."}


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


def test_post_delete_tweet_valid_auth():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        response = client.post(
            "/tweet",
            json={
                "content": "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstri"
            },
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 200
        id = response.json()["id"]
        response = client.delete(
            "/tweet",
            params={"id": id},
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 200
        supabase[1].auth.sign_out()


def test_post_tweet_bigger_than():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        random_string = secrets.token_hex(1201)[:-1]
        response = client.post(
            "/tweet",
            json={"content": random_string},
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 422
    supabase[1].auth.sign_out()


def test_post_tweet_smaller_than():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        random_string = secrets.token_hex(70)[:-1]
        response = client.post(
            "/tweet",
            json={"content": random_string},
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 422
    supabase[1].auth.sign_out()


def test_get_hashtags_no_auth():
    with TestClient(app) as client:
        response = client.get("/hashtag")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }


def test_get_hashtags_valid_auth():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        response = client.get(
            "/hashtag",
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 200
        assert response.json() is not None
    supabase[1].auth.sign_out()


def test_get_trends_no_auth():
    with TestClient(app) as client:
        response = client.get("/hashtag/trends")
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Not authenticated",
        }


def test_get_trends_valid_auth():
    supabase = sign_in_with_password(test_user)
    with TestClient(app) as client:
        response = client.get(
            "/hashtag/trends",
            headers={"Authorization": f"Bearer {supabase[0].session.access_token}"},
        )
        assert response.status_code == 200
        assert response.json() is not None
    supabase[1].auth.sign_out()
