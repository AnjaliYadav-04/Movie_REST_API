"""
URL configuration for mysitenew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
#since we are using django rest framework so we need to import the router which allow us to create routes for our APIs
from rest_framework import routers
from movies.views import MovieViewSet,ActionViewSet,ComedyViewSet,RomancticViewSet
from django.conf.urls.static import static
from django.conf import settings

#router=routers.DefaultRouter()# after creating this router we nee to register the movie view i.e, MovieVIewSet

router=routers.SimpleRouter()

router.register('movies', MovieViewSet, basename='movies')         # all movies
router.register('action', ActionViewSet, basename='action-movies')
router.register('comedy',ComedyViewSet,basename='comedy')
router.register('romantic',RomancticViewSet,basename='romantic')


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
