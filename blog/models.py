from django.db import models
#from datetime import date.today
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to = 'blog/images/', blank=True)
    
    def __str__(self):
        return self.title