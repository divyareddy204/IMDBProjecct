from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from imdb.models import *
from django.shortcuts import render
# Create your views here.
def get_polar_chart_data():
    
    import json
    collection_list=Movie.objects.values_list('box_office_collection_in_crores',flat=True)
    movie_ids=Movie.objects.values_list('movie_id',flat=True)
    polar_chart_data = {
        "datasets": [{
            "data": list(collection_list),
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": list(movie_ids),
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }

def get_one_bar_plot_data():
    import json
    collection_list=Movie.objects.values_list('box_office_collection_in_crores',flat=True)
    movie_ids=Movie.objects.values_list('movie_id',flat=True)
    single_bar_chart_data = {
        "labels": list(movie_ids),
        "dataset":[
            {
        "data": list(collection_list),
        "name": "Single Bar Chart",
        "borderColor": "rgba(0, 243, 255, 0.9)",
        "border_width": "0",
        "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Title'
    }

    
def home(request):
    context=Movie.objects.all()
    return render(request, 'imdb_home.html',{'context':context})

def movie(request):
    context=Actor.objects.all()
    return render(request,'imdb_movie.html',{'context':context})

def actor(request):
    context=Actor.objects.all()
    return render(request,'imdb_actor.html',{'context':context})

def director(request):
    context=Director.objects.all()
    return render(request,'imdb_director.html',){'context':context}

def analytics(request):
    import json
    data = {}
    data = get_one_bar_plot_data()
    data1=get_polar_chart_data()
    data.update(data1)
        
    return render(request,'analytics.html',context = data)



