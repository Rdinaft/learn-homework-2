"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    import csv
    employers = [
        {'name':'Alex', 'age': '22', 'job': 'PR manager'},
        {'name':'Elena', 'age': '34', 'job': 'HR'},
        {'name':'Mike', 'age': '35', 'job': 'Data scientist'},
        {'name':'Maria', 'age': '20', 'job': 'IT specialist'},
    ]

    with open('employers.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for employer in employers:
            writer.writerow(employer)

if __name__ == "__main__":
    main()
