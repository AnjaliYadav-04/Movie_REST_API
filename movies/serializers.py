from rest_framework import serializers
from .models import Moviedata

#create serialezer and to create  serialers we need to create class
#and that class is inherit from the ModelSerializer(IT'S SOmething that serializes your model)
class MovieSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class  Meta:
        model=Moviedata
        #NOw we initialise the fields that we wants the API response
        fields=['id','name','duration','rating','typ','image']#id added by default to the movies
        #once these fields are serialized we need to create views that display the data created by the serializers
        #  then create url associated with that view

