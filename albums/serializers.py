from rest_framework import serializers
from .models import Album
from .services import get_album_songs_count, get_total_songs_duration


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "musician_id",
            "songs_count",
            "total_duration",
        ]

        extra_kwargs = {
            "musician_id": {"read_only": True},
        }

    songs_count = serializers.SerializerMethodField(read_only=True)
    total_duration = serializers.SerializerMethodField(read_only=True)

    def get_songs_count(self, obj: Album):
        return get_album_songs_count(obj)

    def get_total_duration(self, obj: Album):
        return get_total_songs_duration(obj)
