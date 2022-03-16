import pytest
from app import app

def test_func_case_1():
    assert True
def test_func_case_2():
    assert 1 == 1


@pytest.fixture(autouse=True)
def client():
    return app.test_client()

def test_home(client): 
    response = client.get('/')
    assert b'Hello, World!' in response.data  

    assert response.status_code == 200