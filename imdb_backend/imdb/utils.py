from imdb.models import *
def get_one_bar_plot_data():
    import json
    single_bar_chart_data = {
        "labels": ["Sun", "Mon", "Tu", "Wed", "Th", "Fri", "Sat"],
        "dataset":[
            {
        "data": [40, 55, 75, 81, 56, 55, 40],
        "name": "Single Bar Chart",
        "borderColor": "rgba(0, 123, 255, 0.9)",
        "border_width": "0",
        "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'rating of a director'
    }


def get_two_bar_plot_data():
    import json
    multi_bar_plot_data = {
        "labels": ["January", "February", "March", "April", "May", "June",
                   "July"],
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 80, 81, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "My Second dataset",
                "data": [28, 48, 40, 19, 86, 27, 90],
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Title'
    }


def get_multi_line_plot_data():
    import json
    multi_line_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Foods",
            "data": [0, 30, 10, 120, 50, 63, 10],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Electronics",
            "data": [0, 50, 40, 80, 40, 79, 120],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Title'
    }


def get_area_plot_data():
    import json
    area_plot_data = {
        "labels": ["2015", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": [0, 7, 3, 5, 2, 10, 7],
            "label": "Expense",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'rating of a directors'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data():
    import json
    doughnut_graph_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4"
        ]
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data():
    import json

    pie_chart_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green",
            "Green",
            "Green"
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Title'
    }


def get_polar_chart_data():
    movie_ids=Movie.objects.values_list('id',flat=True)
    import json

    polar_chart_data = {
        "datasets": [{
            "data": list(movie_ids),
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": list(movie_ids)
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }


def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows

def populate_actor():
    import json
    object=open('/home/apiiitrkv/Desktop/100_movies/actors_100.json','r') 
    object1=object.read()
    actors_list=json.loads(object1)
    for actor in actors_list:
        Actor.objects.create(actor_id=actor['actor_id'],name=actor['name'],gender=actor['gender'])

def populate_director():
    import json
    object=open('/home/apiiitrkv/Desktop/100_movies/directors_100.json','r') 
    object1=object.read()
    directors_list=json.loads(object1)
    for director in directors_list:
      Director.objects.create(
          name=director['name'],gender=director['gender'],
          no_of_facebook_likes=director['no_of_facebook_likes'])


def populate_movie():
    import json
    import random
    object=open('/home/apiiitrkv/Desktop/100_movies/movies_100.json','r') 
    object1=object.read()
    movies_list=json.loads(object1)

    for movies in movies_list:
        
        movie_obj=Movie.objects.create(
            movie_id=movies["movie_id"],
            name=movies["name"],
            box_office_collection_in_crores=movies["box_office_collection_in_crores"],
            release_date=movies["year_of_release"],
            director=Director.objects.get(name=movies["director_name"]),
            genres=random.choice(movies['genres']),
            country=movies['country'],
            average_rating=movies['average_rating']
            )
        for actor in movies["actors"]:
                Cast.objects.create(
                actor=Actor.objects.get(actor_id = actor["actor_id"]),
                movie=movie_obj,
                role=actor["role"],
                is_debut_movie=actor["is_debut_movie"])

'''#Task-3
def get_no_of_distinct_movies_actor_acted(actor_id):
    
   return Movie.objects.filter(actors=actor_id).distinct().count()
 
 #Task4
def get_movies_directed_by_director(director_obj):
   
   return director_obj.movie_set.all()
   
#Task5
def get_average_rating_of_movie(movie_obj):
   try:
      rate=Rating.objects.get(movie=movie_obj)
      number=1.0*rate.rating_one_count+2*rate.rating_two_count+3*rate.rating_three_count+4*rate.rating_four_count+5*rate.rating_five_count
      sum1=rate.rating_one_count+rate.rating_two_count+rate.rating_three_count+rate.rating_four_count+rate.rating_five_count
      return number/sum1
   except:
      return 0
   
   
   
#Task6
def delete_movie_rating(movie_obj):
   
   return Rating.objects.get(movie=movie_obj).delete()
#movie_obj.rating.delete()
   
#Task7
def get_all_actor_objects_acted_in_given_movies(movie_objs):
   return Actor.objects.filter(movie__in=movie_objs).distinct()
     
#Task8
def update_director_for_given_movie(movie_obj, director_obj):
   
   movie_obj.director=director_obj
   movie_obj.save()
   return 

#Task9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
   
   return Movie.objects.filter(actors__name__contains='john').distinct()

#Task10
def remove_all_actors_from_given_movie(movie_obj):
   
   return movie_obj.actors.clear()
   

#Task11
def get_all_rating_objects_for_given_movies(movie_objs):
   
   return Rating.objects.filter(movie__in=movie_objs)
 
def get_all_distinct_actors_for_given_movie(movie_obj):
   
   return Actor.objects.filter(movie=movie_obj).distinct()
'''
