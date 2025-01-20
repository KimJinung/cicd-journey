from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_greeting():
    response = client.get("/greeting")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
