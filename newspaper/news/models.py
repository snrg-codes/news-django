from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True)
    content = RichTextField()
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


