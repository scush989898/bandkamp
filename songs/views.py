from django.shortcuts import get_object_or_404
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Song
from musicians.models import Musician
from albums.models import Album
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters


class SongFilter(filters.FilterSet):
    min_duration = filters.NumberFilter(field_name="duration", lookup_expr="gte")
    max_duration = filters.NumberFilter(field_name="duration", lookup_expr="lte")

    class Meta:
        model = Song
        fields = ["duration"]


class SongView(ListCreateAPIView):
    serializer_class = SongSerializer
    lookup_url_kwarg = ("musician_id", "album_id")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SongFilter

    def perform_create(self, serializer):
        get_object_or_404(Musician, id=self.kwargs["musician_id"])
        album = get_object_or_404(Album, id=self.kwargs["album_id"])
        return serializer.save(album_id=album)

    def get_queryset(self):
        album = get_object_or_404(Album, id=self.kwargs["album_id"])
        return Song.objects.filter(album_id=album)
