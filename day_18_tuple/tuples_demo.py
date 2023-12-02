from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

is_jukebox_on = True
while is_jukebox_on:
    # album_choice = input("Please chose your album. (Invalid choice exits): ")
    for index, (title, artist, year, song) in enumerate(albums):
        print(f"{index + 1}: {title}")

    # this is same as
    # for index, value in enumerate(albums):
    #     title, artist, year, song = value
    #     print(index, title, artist, year, song)

    choice = int(input("please type a number to chose: "))
    if 1 <= choice <= len(albums):
        songs = albums[choice - 1][SONGS_LIST_INDEX]
        print("Please chose your song")
        for index, (track_number, song) in enumerate(songs):
            print(f"{index + 1}: {song}")
        song_choice = int(input("please select a song: "))
        if 1 <= song_choice <= len(songs):
            title = songs[song_choice - 1][SONG_TITLE_INDEX]
            print(f"playing {title}")
        print('-' * 40)
        print()
        # for index, song in enumerate(songs):
        #     print(f"{index + 1}: {song[1]}")
    else:
        break







