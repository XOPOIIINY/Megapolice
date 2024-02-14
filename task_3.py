import csv

with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))


def find_song_of_artist(artist, data):
    for d in data:
        if artist in d:
            return d[2]
    return False


print('Введите артиста, которого хотите найти')
artist = input()
song = find_song_of_artist(artist, data)
if song:
    print(f'У {artist} найдена песня: {find_song_of_artist(artist, data)}')
else:
    print('К сожалению, ничего не удалось найти')