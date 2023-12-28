class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): an artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method
        :param title: initialize the `title` attribute
        :param artist: An artist attribute representing the song's creator
        :param duration: initial value for the `duration`attribute. Will default to zero if not specified
        """

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using it's track list

    Attributes:
        album_name (str): Name of the album
        year (int): The year of the release of album
        artist (Artist): The artist responsible for the album
            if not specified, artist will default to an artist with
            the name "various artists"
        tracks (List(Song)): A list of the song in the album

    Methods:
        add_song: Used to add new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position):
        """
        Adds song to the track list
        :param song: Name of the song to add
        :param position (optional[int]): position of the song in  the album.
            if specified, the song will be added to that position in the track list.
            Inserting in between other songs if necessary. Other wise the song will
            be added at the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details
    Attributes:
        name (str): The name of the artist
        album (list[Album]): A list of the album by this artist
            The list includes only some albums in this collection.
            It is not an exhaustive list of the artist's published albums

    Methods:
        add_album: Used to add new albums to the artist's album list
        """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Adds a new album to list
        Args:
            album (Album): Album object to add to the list
            If the album is already in the list, it will not be added
            """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # each row contains artist_field, album, year, song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for new artist
                # store the current album in the current artist's collection and create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we've read a new album with current artist
                # store the current in the artist's collection and create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song, 0)

        # after reading the last line of the text file, we will have an album and artist which haven't been stored - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list






if __name__ == '__main__':
    load_data()
