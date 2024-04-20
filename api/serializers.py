from rest_framework import serializers
from api.models import Movie, Actor, Genre, Technician

#Create serializers here
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Actor
        fields = "__all__"

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Genre
        fields = "__all__"

class TechnicianSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Technician
        fields = "__all__"