import mimetypes
from urllib import parse
from flask import Flask, render_template, url_for, request, json, jsonify
# from flask_paginate import Pagination, get_page_parameter
from data import queries
import json
import math
from dotenv import load_dotenv
from data.data_manager import execute_select
from datetime import date

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/shows/most-rated', methods=['POST', 'GET'])
def render_most_rated_page():
    page_number = request.args.get('page', default=1, type=int)
    sort = request.args.get('sort', default="rating", type=str)
    most_rated_shows = queries.get_most_rated_shows(page_number, sort)
    limit_items = 15
    number_of_page = len(queries.get_shows()) // limit_items
    return render_template("most-rated.html", most_rated_shows=most_rated_shows, page_number=page_number,sort=sort, number_of_page=number_of_page)

@app.route('/show/<int:id>')
def detail_movie(id):
    data = queries.get_show_by_id(id)
    seasons = queries.get_seasons_by_show_id(id)
    actors = queries.get_actors_name_by_show_id(id)
    name = []
    for actor in actors:
        name.append(actor['name'])
    actors_name = (', '.join(name))
    trailer = data[0]['trailer']
    if trailer == "No URL":
        video_id = ''
    else:
        url_elem = parse.urlparse(trailer).query
        video_id = parse.parse_qs(url_elem).get('v')[0]
    return render_template("detail-movie.html", data=data[0], id=id, actors_name=actors_name, video_id=video_id, seasons=seasons)

@app.route('/actors')
def get_actors():
    actors_and_their_movies = queries.get_all_actors_and_movies()
    return render_template("actors.html", actors_and_their_movies=actors_and_their_movies)

@app.route('/api/actors/movie')
def get_movie_for_actors():
    name = request.args.get('actorName')
    data = queries.get_actor_and_movie_by_name(name)
    return data

@app.route('/pengiuns')
def render_pengiuns():
    return render_template("penguins.html")

@app.route('/api/penguins')
def get_title_in_season():
    season = request.args.get('season')
    data = queries.get_pengiuns(season)
    return data

@app.route('/ratings')
def ratings():
    title_movies = queries.get_movie_by_rating()
    return render_template("ratings.html",title_movies=title_movies)

@app.route('/ordered_shows')
def ordered_shows():
    sort = request.args.get('sort', default="desc", type=str)
    data = queries.get_title_sort_rating(sort)
    return render_template("ordered-shows.html", data=data, sort=sort)

@app.route('/filter-actors')
def filter_actors():
    genres = queries.get_genres()
    return render_template("filter-actors.html", genres=genres)

# @app.route('/api/actors/')
@app.route('/api/actors')
def get_actors_by_data():
    name = request.args.get('name', default="", type=str)
    genre = request.args.get('genre', default="Action")
    data = queries.get_actors_by_genre_and_name(genre,name.capitalize())
    return data

@app.route('/actors-birthday')
def actors_birthday():
    actors_and_birthday = queries.get_life_actors()
    print(actors_and_birthday)
    return render_template("birthday-actors.html", actors_and_birthday=actors_and_birthday)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
