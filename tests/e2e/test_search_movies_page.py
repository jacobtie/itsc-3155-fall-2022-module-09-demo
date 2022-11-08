from flask.testing import FlaskClient

from src.repositories import movie_repository


def test_search_movie(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data


def test_search_movie_no_results(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    response = test_app.get('/movies/search?query=something')
    response_data = response.data
    assert b'<h2>No movie found!</h2>' in response_data


def test_search_movie_success(test_app: FlaskClient):
    mrs = movie_repository.get_movie_repository()
    mrs.clear()
    mrs.create_movie('Test Movie', 'Test Director', 5)
    response = test_app.get('/movies/search?query=Test+Movie')
    response_data = response.data
    assert b'<h2>Test Movie - Test Director - 5</h2>' in response_data
