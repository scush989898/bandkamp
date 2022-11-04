from ...models import Musician
from albums.models import Album
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random

instruments = [
    "Violão",
    "Violino",
    "Bateria",
    "Guitarra",
    "Piano",
    "ContraBaixo",
    "Viola",
    "Banjo",
]


class Command(BaseCommand):
    help = "Create random musicians and albums"

    def handle(self, *args, **kwargs):
        for i in range(2):
            musician = Musician.objects.create(
                first_name=get_random_string(6),
                last_name=get_random_string(8),
                instrument=random.choices(instruments)[0],
            )
            for j in range(2):
                Album.objects.create(
                    name=get_random_string(10),
                    musician=musician,
                )
