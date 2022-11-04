from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)

    musician = models.ForeignKey(
        "musicians.Musician",
        on_delete=models.CASCADE,
        related_name="albums",
    )
