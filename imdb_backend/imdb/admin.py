from django.contrib import admin

# Register your models here.

from imdb.models import *

admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Rating)