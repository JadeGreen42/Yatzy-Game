from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_roll():
    response = client.get("/roll")
    assert response.status_code == 200

    data = response.json()
    assert "dice" in data
    assert isinstance(data["dice"], list)
    assert len(data["dice"]) == 5

    for value in data["dice"]:
        assert 1 <= value <= 6


def test_score_valid():
    payload = {
        "choice": 12,
        "dice": [6, 6, 6, 6, 6]
    }

    response = client.post("/score", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "score" in data
    assert "is_upper_section" in data


def test_score_invalid_dice_length():
    payload = {
        "choice": 12,
        "dice": [6, 6]  # invalid length
    }

    response = client.post("/score", json=payload)
    assert response.status_code == 422  # validation error


def test_score_invalid_die_value():
    payload = {
        "choice": 12,
        "dice": [6, 6, 6, 6, 10]  # invalid value
    }

    response = client.post("/score", json=payload)
    assert response.status_code == 422