from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from imdb.models import *
from imdb.utils import *
from django.shortcuts import render
# Create your views here.


def get_two_bar_plot_data():
    import json
    male="""select count(*) from imdb_actor as a inner join imdb_cast as c inner join imdb_movie as m ON 
    a.actor_id=c.actor_id and c.movie_id=m.movie_id where(a.gender='male') group by m.release_date"""
    female="""select count(*) from imdb_actor as a inner join imdb_cast as c inner join imdb_movie as m ON 
    a.actor_id=c.actor_id and c.movie_id=m.movie_id where(a.gender='female') group by m.release_date"""
    year="""select m.release_date from imdb_actor as a inner join imdb_cast as c inner join imdb_movie as m ON 
    a.actor_id=c.actor_id and c.movie_id=m.movie_id  group by m.release_date"""

    males_list=execute_sql_query(male)
    females_list=execute_sql_query(female)
    years_list=execute_sql_query(year)
    multi_bar_plot_data = {
        "labels": list(years_list),
        "datasets": [{
                "label": "males",
                "data": list(males_list),
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "females",
                "data": list(females_list),
                "borderColor": "rgb(191, 63, 63)",
                "borderWidth": "0",
                "backgroundColor": "rgb(191, 63, 63)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Male and female actors in a particular year'
    }



def get_area_plot_data():
    import json
    movie="""select average_rating  from imdb_movie where director_id=4"""
    year="""select release_date from imdb_movie where director_id=4"""
    movie_list=execute_sql_query(movie)
    year_list=execute_sql_query(year)
    area_plot_data = {
        "labels": list(year_list),
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": list(movie_list),
            "label": "Expense",
            "backgroundColor": 'rgb(204, 255, 102)',
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
        'area_plot_data_one_title': 'average rating -movie director in a year'

    }
def get_pie_chart_data():
    import json
    male="""select count(*) from imdb_actor group by gender"""
    males_list=execute_sql_query(male)
    pie_chart_data = {
        "datasets": [{
            "data": list(males_list),
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
        "labels": ['male','female']
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'males and female Actors'
    }






def get_doughnut_chart_data():
    import json
    genres="""select distinct(genres) from imdb_movie """
    movie_count="""select count(*) from imdb_movie group by genres"""
    genres_list=execute_sql_query(genres)
    movie_list=execute_sql_query(movie_count)
    doughnut_graph_data = {
        "datasets": [{
            "data":list(movie_list),
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
        "labels":list(genres_list)
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title' :'number of movies in each genre'
    }


def get_multi_line_plot_with_area_data():
    import json
    collections="""select box_office_collection_in_crores from imdb_movie group by release_date"""
    rating="""select average_rating from imdb_movie group by release_date """
    year=""" select release_date from imdb_movie group by release_date """
    collection_list=execute_sql_query(collections)
    rating_list=execute_sql_query(rating)
    year_list=execute_sql_query(year)
    multi_line_plot_with_area_data = {
        "labels":list(year_list),
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "collections dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgb(102, 255, 255)",
                "data": list(collection_list)
            },
            {
                "label": "rating dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": list(rating_list)
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'box office collections and average rating in each year'
    }






def home(request):
    context=Movie.objects.all()
    return render(request, 'imdb_home.html',{'context':context})

def movie(request,movie_id):
    object1=Movie.objects.get(movie_id=movie_id)
    context=object1.actors.filter()
    return render(request,'imdb_movie.html',{'context':context})

def actor(request,actor_id):
    object1=Actor.objects.get(actor_id=actor_id)
    context=object1.movie_set.all()
    return render(request,'imdb_actor.html',{'context':context})

def director(request,director_id):
    context=Movie.objects.filter(director=director_id)
    return render(request,'imdb_director.html',{'context':context})

def analytics(request):
    import json
    data = {}
    data1=get_two_bar_plot_data()
    data.update(data1)
    
    data3=get_area_plot_data()
    data.update(data3)

    data5=get_doughnut_chart_data()
    data.update(data5)

    data6=get_multi_line_plot_with_area_data()
    data.update(data6)
    
    data7=get_pie_chart_data()
    data.update(data7)
    return render(request,'analytics.html',context = data)



