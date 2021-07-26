from django.db import models
from django.db.models import Model
from django.utils import timezone


# Create your models here.

class Video(models.Model):
    videotitle = models.CharField(max_length = 20)
    videodec = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.videotitle,self.id)
