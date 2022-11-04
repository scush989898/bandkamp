from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "id",
            "name",
            "duration",
            "album_id",
        ]
        extra_kwargs = {
            "album_id": {
                "read_only": True,
            },
        }
