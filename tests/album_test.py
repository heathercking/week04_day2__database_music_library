import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("I Walk The Line", "Rockabilly", "Johnny Cash")

    def test_album_has_title(self):
        self.assertEqual("I Walk The Line", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rockabilly", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Johnny Cash", self.album.artist)