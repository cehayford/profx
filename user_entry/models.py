from django.db import models
from django.utils.text import slugify

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=False, blank=False)
    description = models.TextField(max_length = 500)
    date_of_birth = models.DateField()


class ProgLanguage(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class OtherLanguage(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tools(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Databases(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Frameworks(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Skills(models.Model):
    language = models.ForeignKey(ProgLanguage, on_delete=models.CASCADE, related_name='skills')
    other_language = models.ForeignKey(OtherLanguage, on_delete=models.CASCADE, related_name='skills')
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE, related_name='skills')
    database = models.ForeignKey(Databases, on_delete=models.CASCADE, related_name='skills')
    framework = models.ForeignKey(Frameworks, on_delete=models.CASCADE, related_name='skills')

class MediaLinks(models.Model):
    email = models.URLField()
    x = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
