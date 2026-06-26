def test_register(client):
    response = client.post("/auth/register", json={
        "username": "testuser",
        "name": "Test User",
        "gender": "Male",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "password": "secret123"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_register_duplicate_email(client):
    # Register once
    client.post("/auth/register", json={
        "username": "testuser",
        "name": "Test User",
        "gender": "Male",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "password": "secret123"
    })
    # Register again with same email
    response = client.post("/auth/register", json={
        "username": "testuser2",
        "name": "Test User",
        "gender": "Male",
        "email": "test@gmail.com",
        "phone": "9876543211",
        "password": "secret123"
    })
    assert response.status_code == 400

def test_login(client):
    client.post("/auth/register", json={
        "username": "testuser",
        "name": "Test User",
        "gender": "Male",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "password": "secret123"
    })
    response = client.post("/auth/login", data={
        "username": "test@gmail.com",
        "password": "secret123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()