# t = 'a', 'b', 'c'
# print(t)

# welcome = 'Welcome to my nightmare', 'Alice mayer', 1975
# bad = 'bad company', 'bad company', 1974
# budgie = 'Night flight', 'budgie', 1981
# imelda = 'more mayhem', 'Emilda may', 2011
# metallica = 'Ride the lightening', 'Metallica', 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])


# indexing in tuples works same as list, square brackets are used
# item assignment is not supported in tuples
# tuples can be converted to list


# metallica2 = list(metallica)
# metallica2[0] = 'Master of puppets'
# print(metallica2)


# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
#
# table = ['Coffee table', 200, 100, 75, 34.50]
# print(table[1] * table[2])
# # or
# name, length, width, height, price = table
# print(length * width)


albums = [('Welcome to my nightmare', 'Alice mayer', 1975),
           ('bad company', 'bad company', 1974),
           ('Night flight', 'budgie', 1981),
           ('more mayhem', 'Emilda may', 2011),
           ('Ride the lightening', 'Metallica', 1984)]

print(len(albums))

for album in albums:
    album_name, artist, year = album
    print(f"{album_name}, {artist}, {year}")

# most of the time we should use this method to unpack the tuples
for name, artist, yeaar in albums:
    print(f"album: {name}, artist: {artist}, release: {yeaar}")
