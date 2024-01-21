from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Video(models.Model):
    url = EmbedVideoField()

    def __str__(self):
        return self.url
    
