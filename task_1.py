from datetime import datetime, timedelta
import csv

# открытие файла в формате csv (открыл не DictReader, т. к. возникли проблемы со столбцом streams
# (так вывел - \ufeffstreams))
with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))
date = '01.01.2002'
date_of_request = '12.05.2023'
# перевод числа в формат datetime (библиотека встроена!)
date = datetime.strptime(date, "%d.%m.%Y")
date_of_request = datetime.strptime(date_of_request, "%d.%m.%Y")


# функция замены 'unknown' параметров streams
def replace_unknown(date_song, artist, song):
    """

    :param date_song: дата выхода песни
    :param artist: исполнитель песни
    :param song: песня
    :return:
    """
    streams = abs((date_of_request - date_song) / (len(artist) + len(song))) * 10000
    return streams


# ans - список для вывода в файл
ans = [['track_name;artist;streams']]
for d in data[1:]:
    if datetime.strptime(d[-1], "%d.%m.%Y") <= date:
        if not d[0].isdigit():
            d[0] = replace_unknown(d[-1], d[1], d[2])  # вызов функции, если параметр не числовой
        print(f'{d[2]} - {d[1]} - {d[0]}')
        ans.append([f'{d[2]};{d[1]};{d[0]}'])

print(ans)

# запись данных (ans) в ответ - файл вывода
with open('songs_new.csv', 'w', newline='') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerows(ans)
