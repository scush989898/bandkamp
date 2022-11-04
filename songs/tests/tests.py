from rest_framework.test import APITestCase
from albums.models import Album
from musicians.models import Musician


class SongViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.musician_data = {
            "first_name": "Jhon",
            "last_name": "Fruciant",
            "instrument": "Guitarrr",
        }
        cls.album_data = {
            "name": "The Empyrean",
        }
        cls.song1_data = {
            "name": "Before the Beginning",
            "duration": 548,
        }
        cls.song2_data = {
            "name": "Unreachable",
            "duration": 370,
        }
        cls.missing_keys = {}

        cls.musician = {}
        cls.album = {}

    def setUp(self) -> None:
        self.musician = Musician.objects.create(**self.musician_data)
        self.album = Album.objects.create(**self.album_data, musician=self.musician)

    def test_create_song_no_body(self):
        """
        it should not be able to create a song with wrong/missing data
        """
        response = self.client.post(
            f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/",
            self.missing_keys,
        )
        self.assertEqual(response.status_code, 400)

    def test_create_song_invalid_album(self):
        """
        it should not be able to create a song with invalid album id
        """
        response = self.client.post(
            f"/api/musicians/{self.musician.id}/albums/555/songs/",
            self.song1_data,
        )
        self.assertEqual(response.status_code, 404)

    def test_create_song_invalid_musician(self):
        """
        it should not be able to create a song with invalid musician id
        """
        response = self.client.post(
            f"/api/musicians/3000/albums/{self.album.id}/songs/",
            self.song2_data,
        )
        self.assertEqual(response.status_code, 404)

    def test_should_be_able_to_create_song(self):
        """
        it should be able to create a song
        """
        response = self.client.post(
            f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/",
            self.song2_data,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["name"],
            self.song2_data["name"],
        )
        self.assertEqual(
            response.data["duration"],
            self.song2_data["duration"],
        )
        self.assertEqual(response.data["album_id"], self.album.id)

    def test_list_songs_with_invalid_album(self):
        """
        it should not be able to list songs with invalid album id
        """
        response = self.client.get(
            f"/api/musicians/{self.musician.id}/albums/555/songs/"
        )
        self.assertEqual(response.status_code, 404)

    def test_should_list_songs(self):
        """
        it should be list all songs related to the album id
        """
        self.client.post(
            f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/",
            self.song1_data,
        )
        self.client.post(
            f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/",
            self.song2_data,
        )
        response = self.client.get(
            f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)
