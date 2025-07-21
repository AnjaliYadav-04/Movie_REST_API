from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=MovieSerializer

#after adding new field in db we need to create new view for movie type 'action' and after this add this path to urls.py and register the newly created view
#and also change the router from defaultrouter -> SimpleRouter
class ActionViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(typ='action')
    serializer_class=MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(typ='comedy')
    serializer_class=MovieSerializer

class RomancticViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(typ='romantic')
    serializer_class=MovieSerializer    
    