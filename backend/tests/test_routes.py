import secrets

from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

valid_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEZXNvZnMiLCJpYXQiOjE3MTU3OTcwOTEsImV4cCI6MTc0NzMzMzA5MSwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDAwIiwic3ViIjoiaXNlcC5pcHAucHQiLCJBZG1pbiI6IkRlc29mcyJ9.QTx1JeQoP7sHWAwUy6PFQukEi0TszK0zZErtKsI4yU0"

expired_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEZXNvZnMiLCJpYXQiOjE3MTU3OTcwOTEsImV4cCI6MTY4NDE3NDY5MSwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDAwIiwic3ViIjoiaXNlcC5pcHAucHQiLCJBZG1pbiI6IkRlc29mcyJ9.E4NLh3uDr_QrpmBOkVVvXTaw_nVaCWqwvzeQj9bWr4Q"


def test_get_tweets_no_auth():
    response = client.get("/tweet")
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated",
    }


def test_get_tweets_valid_auth():
    response = client.get("/tweet", headers={"Authorization": f"Bearer {valid_jwt}"})
    assert response.status_code == 200
    assert response.json() is not None


def test_get_tweets_expired_auth():
    response = client.get("/tweet", headers={"Authorization": f"Bearer {expired_jwt}"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid token or expired token."}


def test_post_tweet_no_auth():
    response = client.post(
        "/tweet",
        json={"content": "whatever"},
    )
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated",
    }


def test_post_delete_tweet_valid_auth():
    response = client.post(
        "/tweet",
        json={
            "content": "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstri"
        },
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200
    id = response.json()["id"]
    response = client.delete(
        "/tweet", params={"id": id}, headers={"Authorization": f"Bearer {valid_jwt}"}
    )
    assert response.status_code == 200


def test_post_tweet_bigger_than():
    random_string = secrets.token_hex(1201)[:-1]
    response = client.post(
        "/tweet",
        json={"content": random_string},
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 422


def test_post_tweet_smaller_than():
    random_string = secrets.token_hex(70)[:-1]
    response = client.post(
        "/tweet",
        json={"content": random_string},
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 422


def test_get_hashtags_no_auth():
    response = client.get("/hashtag")
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated",
    }


def test_get_hashtags_valid_auth():
    response = client.get("/hashtag", headers={"Authorization": f"Bearer {valid_jwt}"})
    assert response.status_code == 200
    assert response.json() is not None


def test_get_trends_no_auth():
    response = client.get("/hashtag/trends")
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated",
    }


def test_get_trends_valid_auth():
    response = client.get(
        "/hashtag/trends", headers={"Authorization": f"Bearer {valid_jwt}"}
    )
    assert response.status_code == 200
    assert response.json() is not None
