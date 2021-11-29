from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


        
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True, default=None)
    thumnail =  models.ImageField(default="upload.png", blank=True)
    quality = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    time_pub = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.desc[:50]+'...'
        
    def get_absolute_url(self):
        return reverse('ticket_detail',args=[self.id,])
        
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class TicketReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING,max_length=150)
    
    def get_review_rating(self):
        return self.review_rating