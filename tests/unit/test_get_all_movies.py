from src.repositories import movie_repository

mrs = movie_repository.get_movie_repository()


def test_get_all_movies_no_movies():
    mrs.clear()
    movies = mrs.get_all_movies()
    assert len(movies) == 0


def test_get_all_movies_one_movie():
    mrs.clear()
    mrs.create_movie('Test Title 1', 'Test Director 1', 5)
    movies = mrs.get_all_movies()
    assert len(movies) == 1
    assert movies[0].title == 'Test Title 1'


def test_get_all_movies_multiple_movie():
    mrs.clear()
    mrs.create_movie('Test Title 1', 'Test Director 1', 5)
    mrs.create_movie('Test Title 2', 'Test Director 2', 5)
    mrs.create_movie('Test Title 3', 'Test Director 3', 5)
    movies = mrs.get_all_movies()
    assert len(movies) > 1
