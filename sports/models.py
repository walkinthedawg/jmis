from django.db import models
from django.utils import timezone


class Sport(models.Model):
    """
    A single Sport field in the DB
    """
    name = models.CharField(max_length=35)
    desc = models.CharField(max_length=500)
    wiki = models.CharField(max_length=500)
    alt = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images")

    def __unicode__(self):
        return self.title