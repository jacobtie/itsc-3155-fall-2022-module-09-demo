from src.repositories import movie_repository

mrs = movie_repository.get_movie_repository()


def test_create_movie():
    mrs.clear()
    movie = mrs.create_movie('Test Create Movie', 'Test Create Director', 3)
    movies = mrs.get_all_movies()
    assert len(movies) == 1
    assert movies[0].title == 'Test Create Movie'
    assert movies[0].director == 'Test Create Director'
    assert movies[0].rating == 3
