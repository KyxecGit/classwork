otvet = input('Хотите добавить цитату? ')
while otvet != 'нет':
    citata = input('Введите цитату: ')
    avtor = input('Введите автора: ')
    file = open('citata.txt', 'a', encoding='UTF-8')
    file.write(citata + '\n' + avtor + '\n')
    file.close()
    otvet = input('Хотите добавить цитату? ')

with open('citata.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    print(data)


Ванечкин В 2
Петров С 3
Водопьянов М 4
Гитлер А 5
Сталин И 5
Байден Д 2
Зеленский В 3
