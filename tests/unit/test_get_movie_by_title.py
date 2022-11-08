from src.repositories import movie_repository

mrs = movie_repository.get_movie_repository()


def test_get_movie_success():
    mrs.clear()
    movies = mrs.get_movie_by_title('something')
    assert movies is None


def test_get_movie_success():
    mrs.clear()
    mrs.create_movie('Test Title 1', 'Test Director 1', 5)
    movies = mrs.get_movie_by_title('Test Title 1')
    assert movies.title == 'Test Title 1'
    assert movies.director == 'Test Director 1'
    assert movies.rating == 5
