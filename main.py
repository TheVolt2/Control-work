import pandas as pd

# Чтение данных из CSV-файла и их отображение
article = pd.read_csv('data.csv', delimiter=';', names=['top_game', 'fail_game', 'my_games', 'phone_games', 'random_id'])
print(article)

# Функция для переименования данных и сохранения их обратно в CSV-файл
def rename_data():
    a = int(input('Введите номер строки для изменения (начиная с 0): '))
    b = int(input('Введите номер столбца для изменения (начиная с 0): '))
    rename = input('Введите новое значение: ')
    article.iloc[a, b] = rename
    article.to_csv("data.csv", index=False, sep=";")
    print("Данные успешно обновлены и сохранены в файл data.csv")

# Функция для поиска данных
def search_data():
    koordinata_1 = int(input('Введите номер строки для поиска (начиная с 0): '))
    koordinata_2 = input('Введите название столбца для поиска (top_game, fail_game, my_games, phone_games, random_id): ')
    print(article.at[koordinata_1, koordinata_2])

# Выбор пользователя для выполнения функции
func = int(input('Введите номер функции: 1 - rename_data, 2 - search_data: '))

# Вызов соответствующей функции в зависимости от выбора пользователя
if func == 1:
    rename_data()
elif func == 2:
    search_data()
else:
    print("Неверный номер функции")

# Отображение обновленных данных
print(article)
