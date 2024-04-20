from django.contrib import admin
from api.models import Movie, Actor, Genre, Technician

class MovieAdmin(admin.ModelAdmin):
    list_display=('name','year_of_release', 'user_rating')
    search_fields=('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display=('name','gender','movie')
    list_filter=('movie',)

class GenreAdmin(admin.ModelAdmin):
    list_display=('name','movie')
    list_filter=('movie',)


class TechnicianAdmin(admin.ModelAdmin):
    list_display=('name','role','movie')
    list_filter=('movie',)

# Register your models here.
admin.site.register(Movie,MovieAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Technician,TechnicianAdmin)
