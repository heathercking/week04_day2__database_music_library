import pdb
from models.album import Album
from models.artist import Artist
from repositories import album_repository

import repositories.artist_repository as artist_repository


artist_1 = Artist("Johnny", "Cash")
artist_repository.save(artist_1)

album_1 = Album("I Walk The Line", "Rockabilly", artist_1)
album_repository.save(album_1)

pdb.set_trace()