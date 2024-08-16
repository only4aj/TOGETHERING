from django.db import models
from embed_video.fields import EmbedVideoField
import uuid

# Create your models here.

class Video(models.Model):
    room_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    url = EmbedVideoField(blank=True,null=True)

    def __str__(self):
        return self.url
    
