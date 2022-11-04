from albums.serializers import AlbumSerializer
from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    instrument = serializers.CharField(max_length=255)
    albums = AlbumSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
