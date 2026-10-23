from django.db import models

class Movie(models.Model):
    title= models.Charfield(max_length= 200)
    descriptions= models.TextField()
    image_url= models.URLField(max_length=500)
