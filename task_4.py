import csv

# открытие файла в формате csv (открыл не DictReader, т. к. возникли проблемы со столбцом streams
# (так вывел - \ufeffstreams))
with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))

russian_artists = []  # русские исполнители
foreign_artists = []  # зарубежные исполнители
alphabet = 'цукенгшщзхъфывапролджэюбьтимсчяё'
for d in data[1:]:
    rus = False  # флаг для остановки цикла по условию
    for a in alphabet:
        if a in d[1]:
            rus = True
    if rus:
        russian_artists.append(d[1])
    else:
        foreign_artists.append(d[1])

# запись русских исполнителей в файл txt
with open('russian_artists.txt', 'w', encoding='utf-8') as r_f:
    for r in russian_artists:
        r_f.write(r + '\n')

# запись зарубежных исполнителей в файл txt
with open('foreign_artists.txt', 'w', encoding='utf-8') as f_f:
    for f in foreign_artists:
        f_f.write(f + '\n')

# вывод ответа на задачу (ещё одного, да)
print(f'Количество российских исполнителей: {len(russian_artists)}')
print(f'Количество иностранных исполнителей: {len(foreign_artists)}')