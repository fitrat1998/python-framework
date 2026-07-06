import pytest

def test_basic_route_adding(app):

    @app.route('/home')
    def home(req, resp):
        resp.text = "Hello from home page"

def test_dublicate_routes_throws_exception(app):

    @app.route('/home')
    def home(req, resp):
        resp.text = "Hello from home page"

    with pytest.raises(AssertionError):
        @app.route('/home')
        def home(req, resp):
            resp.text = "Hello from home page2"

def test_resuests_can_be_sent_by_test_client(app, test_client):
    @app.route('/home')
    def home(req, resp):
        resp.text = "Hello from home page"

    response = test_client.get('http://testserver/home')

    assert response.text == "Hello from home page"

def test_parametrized_routing(app, test_client):
    @app.route('/hello/{name}')
    def greeting(request, response, name):
        response.text = f"Hello from {name}"

    assert test_client.get('http://testserver/hello/Ahror').text == "Hello from Ahror"
    assert test_client.get('http://testserver/hello/Asliddin').text == "Hello from Asliddin"

def test_default_response(test_client):
    response =  test_client.get('http://testserver/nonexistent/')

    assert response.text  == "Not Found"
    assert response.status_code == 404

def test_class_based_get(app, test_client):
    @app.route('/books')
    class Books:
        def get(self, req, resp):
            resp.text = "Hello from books page"

    assert test_client.get('http://testserver/books').text == "Hello from books page"


def test_class_based_post(app, test_client):
    @app.route('/books')
    class Books:
        def post(self, req, resp):
            resp.text = "Endpoint to create a book"

    assert test_client.post('http://testserver/books').text == "Endpoint to create a book"


def test_class_based_method_not_allowed(app, test_client):
    @app.route('/books')
    class Books:
        def post(self, req, resp):
            resp.text = "Endpoint to create a book"

    response = test_client.get('http://testserver/books')

    assert response.text  == "Method not allowed"
    assert response.status_code == 405