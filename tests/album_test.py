import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("The Dark Side of the Moon", "Rock", "Pink Floyd")
    
    def test_album_has_title(self):
        self.assertEqual("The Dark Side of the Moon", self.album.title)
    
    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Pink Floyd", self.album.artist)