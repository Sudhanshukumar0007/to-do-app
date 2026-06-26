import pytest

@pytest.fixture
def auth_client(client):
    # Register and login, return client with auth header
    client.post("/auth/register", json={
        "username": "taskuser",
        "name": "Task User",
        "gender": "Male",
        "email": "taskuser@gmail.com",
        "phone": "9876543211",
        "password": "secret123"
    })
    response = client.post("/auth/login", data={
        "username": "taskuser@gmail.com",
        "password": "secret123"
    })
    token = response.json()["access_token"]
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client

def test_create_task(auth_client):
    response = auth_client.post("/tasks/", json={
        "title": "Study pytest",
        "category": "Learning",
        "deadline": "2026-12-01",
        "status": "Ongoing",
        "priority": "High"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Study pytest"
    assert response.json()["priority"] == "High"

def test_get_tasks(auth_client):
    response = auth_client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task(auth_client):
    # Create first
    create = auth_client.post("/tasks/", json={
        "title": "Old title",
        "category": "Learning",
        "deadline": "2026-12-01",
        "status": "Pending",
        "priority": "Low"
    })
    task_id = create.json()["id"]

    # Then update
    response = auth_client.put(f"/tasks/{task_id}", json={
        "status": "Completed"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "Completed"
    assert response.json()["title"] == "Old title"  # unchanged fields stay

def test_delete_task(auth_client):
    create = auth_client.post("/tasks/", json={
        "title": "Delete me",
        "category": "Daily chores",
        "deadline": "2026-12-01",
        "status": "Pending",
        "priority": "Low"
    })
    task_id = create.json()["id"]

    response = auth_client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

def test_get_tasks_unauthenticated(client):
    response = client.get("/tasks/")
    assert response.status_code == 401