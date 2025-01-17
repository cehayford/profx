from django.db import models

# Create your models here.

class MediaLinks(models.Model):
    email = models.URLField()
    x = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
