from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    time_written = models.DateTimeField(default=datetime.now, blank=False)
    content = HTMLField()
    image_exp = models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=100)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
