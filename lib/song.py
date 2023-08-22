class Song:
    # Class attributes
    count = 0  # To keep track of the number of songs
    genres = []  # To store unique genres
    artists = []  # To store unique artists
    genre_count = {}  # To count songs per genre
    artist_count = {}  # To count songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the count of songs
        self.__class__.add_song_to_count()

        # Add the genre to the list of genres if it's unique
        self.__class__.add_to_genres(genre)

        # Add the artist to the list of artists if it's unique
        self.__class__.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}
        for genre in cls.genres:
            cls.genre_count[genre] = 0
        for song in cls.__subclasses__():
            cls.genre_count[song.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}
        for artist in cls.artists:
            cls.artist_count[artist] = 0
        for song in cls.__subclasses__():
            cls.artist_count[song.artist] += 1
