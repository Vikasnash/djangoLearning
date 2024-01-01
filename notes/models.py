from django.db import models


# Create your models here.
class Notes(models.Model):
    """"this is first model and class name is Note,
    it inherits from models.Model

    tittle text and created is created using the shell"""
    title = models.CharField(max_length=200) ## requires max length
    text = models.TextField()   #this does not require max lenght like char field does
    created = models.DateTimeField(auto_now_add=True)  # this will be correctly populated automatically
    ## we should run makemigration post creating any model
