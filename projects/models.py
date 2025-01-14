from django.db import models
import os
from uuid import uuid4

# Create your models here.
class Projects(models.Model):
    id= models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=200)
    technology = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    hostlink = models.URLField()
    github_link = models.URLField()

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        image_fields = [field for field in self._meta.fields if isinstance(field, models.ImageField)]
        for field in image_fields:
            file_path = getattr(self, field.name).path
            print(file_path)
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)