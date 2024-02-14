import csv

# открытие файла в формате csv (открыл не DictReader, т. к. возникли проблемы со столбцом streams
# (так вывел - \ufeffstreams))
with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))


# функция нахождения песни артиста (первой попавшееся)
def find_song_of_artist(artist, data):
    """

    :param artist: исполнитель
    :param data: данные
    :return: либо False, либо песня артиста
    """
    for d in data:
        if artist in d:
            return d[2]
    return False


# диалог с пользователем и вывод ответа
print('Введите артиста, которого хотите найти')
artist = input()
song = find_song_of_artist(artist, data)
if song:
    print(f'У {artist} найдена песня: {find_song_of_artist(artist, data)}')
else:
    print('К сожалению, ничего не удалось найти')