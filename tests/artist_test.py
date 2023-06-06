import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Pink Floyd")
    
    def test_artist_has_name(self):
        self.assertEqual("Pink Floyd", self.artist.name)