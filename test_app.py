from app import app

def test_home_returns_expected_message():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello! Flask application is running."

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
