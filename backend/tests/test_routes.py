from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

valid_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqd3QtcHl0aG9uLXRlc3RpbmciLCJpYXQiOjE3MTU3ODcxNzgsImV4cCI6MTc0NzMyMzE3OCwiYXVkIjoiMTI3LjAuMC4xOjUwMDAiLCJzdWIiOiJkZXNvZnNAaXNlcC5pcHAucHQiLCJBZG1pbiI6IkRlc29mc19NMUJfMyJ9.icG9BcuAILKjs-A34AgXONS53CdCo6QIYpahGlELKDY"

expired_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqd3QtcHl0aG9uLXRlc3RpbmciLCJpYXQiOjE3MTU1Mjc5NzgsImV4cCI6MTc0NzE1MDM3OCwiYXVkIjoiMTI3LjAuMC4xOjUwMDAiLCJzdWIiOiJkZXNvZnNAaXNlcC5pcHAucHQiLCJBZG1pbiI6IkRlc29mc19NMUJfMyJ9.GvkVQJCR0HcqD4VFiznZtg5-EmG5T0CNI-p0z5sjCgE"


def test_get_tweets():
    response = client.get("/tweet")
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated",
    }

    response = client.get("/tweet", headers={"Authorization": f"Bearer {valid_jwt}"})
    assert response.status_code == 200
    assert response.json() != []