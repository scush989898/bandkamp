from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "albums",
        ]
        extra_kwargs = {
            "albums": {
                "read_only": True,
            }
        }
