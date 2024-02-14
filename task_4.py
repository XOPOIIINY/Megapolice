import csv

with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))

russian_artists = []
foreign_artists = []
alphabet = 'цукенгшщзхъфывапролджэюбьтимсчяё'
for d in data[1:]:
    rus = False
    for a in alphabet:
        if a in d[1]:
            rus = True
    if rus:
        russian_artists.append(d[1])
    else:
        foreign_artists.append(d[1])
print(russian_artists)
with open('russian_artists.txt', 'w', encoding='utf-8') as r_f:
    for r in russian_artists:
        r_f.write(r + '\n')

with open('foreign_artists.txt', 'w', encoding='utf-8') as f_f:
    for f in foreign_artists:
        f_f.write(f + '\n')

print(f'Количество российских исполнителей: {len(russian_artists)}')
print(f'Количество иностранных исполнителей: {len(foreign_artists)}')