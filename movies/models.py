from django.db import models

# Create your models here.
class Moviedata(models.Model):
    def __str__(self):
       return self.name  
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    #now do the migration using cmd/terminal affter adding new fiels in database -> make special king of views in views.py for action movies
    typ=models.CharField(max_length=200,default='action')

    #we can add image field in our API we need a package which allow us to work with images in API and that packge is "pillow"
    #to intall the package "pillow" we need to simply type the following command in cmd/terminal i.e, "pip install pillow" ->enter

    #now add new field here ie., image

    image=models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg') #since we uses API here so we need to serialize this particular imagw field in serialzer.py file and then create a field for that 
    #for eg "image" then add that filld in field section also in serilizer.py
    #now create a folder in your root directory where all images are stores
    #then connect that directory to setting.py file so that your django project fetch them form the meadia directory
    #for that initilize or create media root in setting.py file as "MEDIA_ROOT=os.path.join(BASE_DIR,'media')" :this code get the BASE dierectory path from your os and join them with the media directory
    #then defime MEDIA_URL -> add static orth to url.py
    