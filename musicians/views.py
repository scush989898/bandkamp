from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Musician
from .serializers import MusicianSerializer


class MusicianView(ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    lookup_url_kwarg = "musician_id"


class MusicianAlbumView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    lookup_url_kwarg = "musician_id"

    def get_queryset(self):
        musician = get_object_or_404(Musician, id=self.kwargs["musician_id"])
        return Album.objects.filter(musician=musician)

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, id=self.kwargs["musician_id"])
        return serializer.save(musician=musician)
