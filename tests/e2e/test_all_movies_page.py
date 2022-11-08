from flask.testing import FlaskClient

from src.repositories import movie_repository


def test_all_movies_empty(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
    assert b'<h2>No movies found!</h2>' in response_data


def test_all_movies_movies(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    mrs.create_movie('Test Movie', 'Test Director', 5)
    response = test_app.get('/movies')
    response_data = response.data
    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
    assert b'<td>Test Movie</td>' in response_data
