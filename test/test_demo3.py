import pytest
import requests

BASE_URL = "http://api.example.com"


@pytest.fixture(scope="module")
def user_data():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }


@pytest.fixture(scope="module")
def created_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201
    return response.json()


def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data
    assert response_data["name"] == user_data["name"]
    assert response_data["email"] == user_data["email"]


def test_get_user(created_user):
    user_id = created_user["id"]
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == user_id
    assert response_data["name"] == created_user["name"]
    assert response_data["email"] == created_user["email"]


def test_delete_user(created_user):
    user_id = created_user["id"]
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 204

    # Verify the user has been deleted
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
