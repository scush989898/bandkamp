from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instrument = models.CharField(max_length=255)

