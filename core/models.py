from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) -> str:
        
        return self.name
class Article(models.Model):

    STATUS = (
        (0, 'Draft'),
        (1, 'Published')
    )

    title = models.CharField(max_length = 225, unique = True)

    subtitle = models.CharField(max_length = 225, blank = True)

    slug = models.SlugField(max_length = 225, unique = True)

    thumbnail = CloudinaryField('thumbnail')

    meta_description = models.CharField(max_length = 225, blank = True)

    content = RichTextField()

    status = models.IntegerField(choices = STATUS, default = 0)

    tags = models.ManyToManyField(Tag, blank = True)

    date_created = models.DateTimeField(auto_now_add = True)

    date_published = models.DateTimeField(blank=True, null=True)

    date_modified = models.DateTimeField(auto_now = True)

    class Meta:

        ordering = ['-date_published']

    def __str__(self) -> str:
        
        return self.title

