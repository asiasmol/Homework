# from data import data_manager
from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated_shows(page_number, sort):
    return data_manager.execute_select(f"""SELECT s.id, s.title, year, s.runtime, ROUND(s.rating,1) AS rating, 
        STRING_AGG (g.name, ',') genre, coalesce(s.trailer, 'No URL') AS trailer, coalesce(s.homepage, 'No URL') AS homepage 
        FROM public.shows AS s
        JOIN public.show_genres AS sg ON s.id=sg.show_id
        JOIN public.genres AS g ON sg.genre_id = g.id
        GROUP BY s.id
        ORDER BY {sort}
        OFFSET (( %(page_number)s -1) * 15) LIMIT 15 """, variables={'page_number': page_number})


def get_show_by_id(id):
    return data_manager.execute_select(f""" SELECT shows.title, shows.year, shows.runtime, ROUND(shows.rating,1) AS rating, shows.overview,
        STRING_AGG (genres.name, ',') genre, coalesce(shows.trailer, 'No URL') AS trailer
        FROM public.shows 
        JOIN public.show_genres ON shows.id=show_genres.show_id
        JOIN public.genres ON show_genres.genre_id = genres.id
        WHERE shows.id = {id}
        GROUP BY shows.id
        """)

def get_actors_name_by_show_id(id):
    return data_manager.execute_select(f"""SELECT actors.name
        FROM public.show_characters
        JOIN public.actors ON actors.id = show_characters.actor_id
        WHERE show_characters.show_id = {id}
        LIMIT 3
    """)

def get_seasons_by_show_id(id):
    return data_manager.execute_select(f""" SELECT title, coalesce(overview, '') AS overview, season_number
    FROM seasons
    WHERE show_id = {id}
    ORDER BY season_number
    """)


def get_actor_and_movie_by_name(name):
    return data_manager.execute_select(f""" SELECT actors.name, STRING_AGG(shows.title, ', ') AS title
        FROM actors
        JOIN show_characters ON show_characters.actor_id = actors.id
        JOIN shows ON shows.id = show_characters.show_id
        WHERE actors.name = '{name}'
        GROUP BY actors.id
        LIMIT 1
    """, fetchall=False)

def get_all_actors_and_movies():
    return data_manager.execute_select(f""" SELECT name, STRING_AGG(shows.title, ', ') AS title
        FROM actors
        JOIN show_characters ON show_characters.actor_id = actors.id
        JOIN shows ON shows.id = show_characters.show_id
        GROUP BY actors.id
        ORDER BY birthday
        LIMIT 100
    """)

def get_pengiuns(season):
    return data_manager.execute_select(f""" SELECT episodes.title, episodes.overview
        FROM episodes
        JOIN seasons ON seasons.id = episodes.season_id
        JOIN shows ON shows.id = seasons.show_id
        WHERE shows.title = 'The Penguins of Madagascar'
        AND seasons.title = '{season}'
        """)

def get_movie_by_rating():
    return data_manager.execute_select(f"""SELECT shows.title, COUNT(show_characters.actor_id) AS quantity_actors, 
        (shows.rating - (SELECT AVG(rating) from shows)) AS ode
        FROM shows
        JOIN show_characters ON show_characters.show_id = shows.id
        WHERE shows.rating != (SELECT AVG(shows.rating) FROM shows)
        GROUP BY shows.title, shows.rating
        ORDER BY quantity_actors DESC
        LIMIT 10
        """)

def get_genres():
    return data_manager.execute_select(f"""SELECT DISTINCT name FROM genres ORDER BY name""")
def get_title_sort_rating(sort):
    return data_manager.execute_select(f"""SELECT shows.title, ROUND(shows.rating) AS rating, COUNT(episodes.episode_number) AS episodes
        FROM shows
        JOIN seasons ON seasons.show_id = shows.id
        JOIN episodes ON episodes.season_id = seasons.id
        GROUP BY shows.id
        ORDER BY episodes {sort}
        LIMIT 10
        """)


def get_actors_by_genre_and_name(genre, name):
    return data_manager.execute_select(f"""SELECT actors.name AS name, genres.name AS genre
        FROM shows
        JOIN show_characters ON show_characters.show_id = shows.id
        JOIN actors ON actors.id = show_characters.actor_id
        JOIN show_genres ON show_genres.show_id = shows.id
        JOIN genres ON genres.id = show_genres.genre_id
        WHERE genres.name = '{genre}' AND actors.name LIKE '{name}%' 
        LIMIT 20
        """)

def get_life_actors():
    return data_manager.execute_select(f"""SELECT name, birthday, EXTRACT(day from birthday) AS day
        FROM actors
        WHERE death IS NULL
        ORDER BY birthday
            """)

def get_episode_by_data(start, end):
    return data_manager.execute_select(f"""SELECT episodes.title
        FROM shows
        JOIN seasons ON seasons.show_id = shows.id
        JOIN episodes ON episodes.season_id = seasons.id
        WHERE shows.year BETWEEN '{start}' AND '{end}'
        LIMIT 100
                """)