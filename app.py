from flask import Flask, abort, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movies=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating', type=int)
    if not title or not director or not rating or rating < 1 or rating > 5:
        abort(400)
    movie_repository.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    query = request.args.get('query')
    if not query:
        return render_template('search_movies.html', search_active=True)
    movie = movie_repository.get_movie_by_title(query)
    return render_template('search_movies.html', search_active=True, movie=movie, has_searched=True)
