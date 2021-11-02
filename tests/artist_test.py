import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Johnny Cash")

    def test_artist_has_name(self):
        self.assertEqual("Johnny Cash", self.artist.name)