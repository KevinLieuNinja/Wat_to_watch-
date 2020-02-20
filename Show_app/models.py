from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Give a better Title"

        if len(postData['network']) < 2:
            errors['network'] = "Give a valid network"

        if len(postData['release_date']) < 2:
            errors['release_date'] = "Not a valid year"

        if len(postData['description']) < 10:
            errors['description'] = "Not enough words to be shared"

        return errors

class Show(models.Model):
    title = models.CharField(max_length =45)
    network = models.CharField(max_length = 45)
    release_date = models.IntegerField(default = 0)
    description = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()