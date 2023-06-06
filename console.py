import pdb
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
from models.artist import Artist

pdb.set_trace()
artist_1 = Artist("The Beatles")
artist_repository.save(artist_1)



