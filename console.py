import pdb
from models.album import Album
from models.artist import Artist
# from repositories import album_repository

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist("Johnny", "Cash")
artist_repository.save(artist_1)

artist_2 = Artist("Eva", "Cassidy")
artist_repository.save(artist_2)

album_1 = Album("I Walk The Line", "Rockabilly", artist_1)
album_repository.save(album_1)

new_artist = artist_repository.find_artist(artist_1.id)
print(new_artist.first_name)


pdb.set_trace()