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
