from django.shortcuts import render
from rest_framework import viewsets
from api.models import Movie,Actor,Genre , Technician
from api.serializers import MovieSerializer,ActorSerializer,GenreSerializer, TechnicianSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class MovieViewvSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class= MovieSerializer

    #movies/movieId/actors
    @action(detail=True,methods=['get'])
    def actors (self,request,pk=None):
        try:
            movie=Movie.objects.get(pk=pk)
            act=Actor.objects.filter(movie=movie)
            act_serializer=ActorSerializer(act,many=True,context={'request':request})
            return Response(act_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Movie does not exist , Check your Movie id !!! Error'
            })

    #movies/movieId/genres    
    @action(detail=True,methods=['get'])
    def genres (self,request,pk=None):
        try:
            movie=Movie.objects.get(pk=pk)
            gen=Genre.objects.filter(movie=movie)
            gen_serializer=GenreSerializer(gen,many=True,context={'request':request})
            return Response(gen_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Movie does not exist , Check your Movie id !!! Error'
            })
        
    #movies/movieId/technicians   
    @action(detail=True,methods=['get'])
    def technicians (self,request,pk=None):
        try:
            movie=Movie.objects.get(pk=pk)
            tech=Technician.objects.filter(movie=movie)
            tech_serializer=TechnicianSerializer(tech,many=True,context={'request':request})
            return Response(tech_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Movie does not exist , Check your Movie id !!! Error'
            })



class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class= ActorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class= GenreSerializer

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class= TechnicianSerializer


