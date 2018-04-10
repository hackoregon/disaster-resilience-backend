from django.db import models

# Create your models here.
class Song(models.Model):
    release_date = models.DateTimeField()
    title = models.CharField(max_length=100, blank=True, default='')
    album = models.TextField()
    writer = models.TextField()

    class Meta:
        ordering = ('release_date',)
