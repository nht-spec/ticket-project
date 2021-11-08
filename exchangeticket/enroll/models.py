from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    thumnail =  models.ImageField(default="upload.png", blank=True)
    quality = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    time_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.desc[:50]+'...'
        
        


# , upload_to = "images/