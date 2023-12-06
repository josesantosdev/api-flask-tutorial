import pytest
import json

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_create_one_books(client):
    payload = json.dumps({
        "autor": "Paulo Coelho",
        "title": "A espiã",
        "prateleira": "A"
    })

    header = {"Content-Type": "application/json"}

    response = client.post(
        '/books',
        data=payload,
        headers=header
    )

    assert response.status_code == 201


def test_create_a_list_of_books(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps([{
        "autor": "Paulo Coelho",
        "title": "A espiã",
        "prateleira": "A"
    }, {
        "autor": "Robert C. Martin",
        "title": "Código limpo: habilidades práticas do Agile software",
        "prateleira": "C"
    }, {
        "autor": "George R. R. Martin",
        "title": "A Guerra dos Tronos",
        "prateleira": "A"
    }])

    response = client.post(
        '/books',
        headers=header,
        data=payload

    )

    assert response.status_code == 201

def test_get_all_books(client):
    response = client.get('/books')
    data = json.loads(response.data.decode('utf-8'))
    assert data is list and response.status_code == 200

def test_get_one_book(client):
    response = client.get('/books')
    data = json.loads(response.data.decode('utf-8'))
    assert data is dict
    assert response.status_code == 200

def test_edit_all_book_information(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps({
        "autor": "Miguel de Cervantes",
        "title": "Dom Quixote",
        "prateleira": "D"
    })
    response = client.post(
        '/books/1',
        headers=header,
        data=payload
    )
    data = json.loads(response.data.decode('uft-8'))
    assert data['autor'] == "Miguel de Cervantes"
    assert data['title'] == "Dom Quixote"
    assert data['prateleira'] == "D"
    assert response.status_code == 201


def test_edit_one_book_information(client):
    header = {"Content-Type": "application/json"}
    payload = json.dumps({
        "prateleira": "M"
    })
    response = client.put(
        '/books/2',
        headers=header,
        data=payload
    )
    data = json.loads(response.data.decode('uft-8'))
    assert data['prateleira'] == "M"
    assert response.status_code == 201

def test_delete_one_book(client):
    response = client.delete('/book/1')
    assert response.status_code == 201