from datetime import datetime, timedelta
import csv

with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))
date = '01.01.2002'
date_of_request = '12.05.2023'
date = datetime.strptime(date, "%d.%m.%Y")
date_of_request = datetime.strptime(date_of_request, "%d.%m.%Y")


def replace_unknown(date_now, artist, song):
    streams = abs((date_of_request - date_now) / (len(artist) + len(song))) * 10000
    return streams


ans = [['track_name;artist;streams']]
# столбец stream крякнут (не моя вина), поэтому название его - \ufeffstreams
for d in data[1:]:
    if datetime.strptime(d[-1], "%d.%m.%Y") <= date:
        if not d[0].isdigit():
            d[0] = replace_unknown(d[-1], d[1], d[2])
        print(f'{d[2]} - {d[1]} - {d[0]}')
        ans.append([f'{d[2]};{d[1]};{d[0]}'])

print(ans)

with open('songs_new.csv', 'w', newline='') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerows(ans)
