from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user is deleted, so will his/her posts

    class Meta:
      verbose_name_plural = "entries" # correcting the standard auto-assigned 'entrys'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('home')


