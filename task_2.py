from datetime import datetime, timedelta
import csv

# открытие файла в формате csv (открыл не DictReader, т. к. возникли проблемы со столбцом streams
# (так вывел - \ufeffstreams))
with open('songs.csv', 'r', encoding='utf-8') as csv_f:
    data = list(csv.reader(csv_f, delimiter=';'))


# сортировка пузырьком, направленная на сортировку ТОЛЬКО данных времени в таблице (двумерном массиве)
def bubble_sort(data):
    """

    :param data: список для сортировки (в формате списка списков)
    :return: отсортированный список
    """
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if datetime.strptime(data[j][-1], '%d.%m.%Y') < datetime.strptime(data[j + 1][-1], '%d.%m.%Y'):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data[::-1]  # по возрастанию


# вывод
sorted_data = bubble_sort(data[1:])
print(f'{1} {sorted_data[0][2]}, {sorted_data[0][1]}, {sorted_data[0][0]}')
print(f'{2} {sorted_data[1][2]}, {sorted_data[1][1]}, {sorted_data[1][0]}')
print(f'{3} {sorted_data[2][2]}, {sorted_data[2][1]}, {sorted_data[2][0]}')
print(f'{4} {sorted_data[3][2]}, {sorted_data[3][1]}, {sorted_data[3][0]}')
print(f'{5} {sorted_data[4][2]}, {sorted_data[4][1]}, {sorted_data[4][0]}')