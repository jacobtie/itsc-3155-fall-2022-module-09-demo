from flask.testing import FlaskClient

from src.repositories import movie_repository


def test_create_movie_success(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    response = test_app.post('/movies', data={
        'title': 'Test title',
        'director': 'Test director',
        'rating': 3,
    }, follow_redirects=True)
    response_data = response.data

    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
    assert b'<td>Test title</td>' in response_data


def test_create_movie_failure(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    response = test_app.post('/movies', data={}, follow_redirects=True)

    assert response.status_code == 400
