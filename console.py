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
album_3 = Album("Nightbird", "Soul", artist_2)
album_repository.save(album_3)

found_artist = artist_repository.find_artist(artist_1.id)


found_album = album_repository.find_album(album_1.id)


artist_repository.find_all_artists()  


album_repository.find_albums_by_artist(artist_1.id)

artist_2.last_name = "Bloom"
artist_repository.edit_artist(artist_2)

artists = artist_repository.find_all_artists()
for artist in artists:
    print(artist.__dict__)

albums = artist_repository.find_albums_by_artist(artist_1)
for album in albums:
    print(album.__dict__)

album_3.title = "Nightingale"
album_repository.edit_album(album_3)


artist_repository.delete_artist(artist_1.id)
album_repository.delete_album(album_1.id)


pdb.set_trace()