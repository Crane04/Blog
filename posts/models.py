from django.db import models
from datetime import datetime

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    time_written = models.DateTimeField(default=datetime.now, blank=False)
    content = models.TextField(max_length=999999999999999999999)
    image_exp = models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=100)
    is_featured = models.BooleanField(default=False)
