import pytest
from flask import json
from flow.source.app import app

# filepath: flow/source/test_app.py


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_task_1_api(client):
    response = client.get("/task_1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "Task 1 is running:  "


def test_task_2_api(client):
    test_data = {"key": "value"}
    response = client.post("/task_2", json=test_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "Task 2 is running"
    assert data["data"] == test_data
