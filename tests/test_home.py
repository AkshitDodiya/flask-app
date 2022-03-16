import pytest
from app import app

@pytest.fixture(autouse=True)
def client():
    return app.test_client()

def test_home(client): 
    response = client.get('/')
    assert b'Hello, World!' in response.data  

    assert response.status_code == 200