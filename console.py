import pdb
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
from models.artist import Artist

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("The Beatles")
artist_repository.save(artist_1)

album_1 = Album("Abbey Road", "Rock", artist_1)
album_repository.save(album_1)

# pdb.set_trace()
# album_repository.delete_all()
# artist_repository.delete_all()

# pdb.set_trace()
artists = artist_repository.select_all()
albums = album_repository.select_all()

# pdb.set_trace()
album_id = album_repository.select(album_1.id)
artist_id = artist_repository.select(artist_1.id)