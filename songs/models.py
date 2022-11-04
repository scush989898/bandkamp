from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    album_id = models.ForeignKey(
        "albums.Album",
        on_delete=models.CASCADE,
        related_name="songs",
    )
