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
album_2 = Album("Happiness Is You", "Rockabilly", artist_1)
album_repository.save(album_2)
album_3 = Album("Nightbird", "Rockabilly", artist_2)
album_repository.save(album_3)

# found_artist = artist_repository.find_artist(artist_1.id)
# print(found_artist.first_name)

# found_album = album_repository.find_album(album_1.id)
# print(found_album.__dict__)

# artist_repository.find_all_artists()  
# print(album_repository.find_all_albums())

# album_repository.find_albums_by_artist(artist_1.id)

artist_2 = Artist("Eva", "Bloom")
artist_repository.edit_artist(artist_2)


pdb.set_trace()