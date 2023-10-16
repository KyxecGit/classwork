Задание 1. «Долголетие: оформление заказа»


1.4. Программа после исправления ошибок:
time = int(input('Введите текущее время в часах:'))
while time >= 10 and time < 24:
    print('Мы открыты')
    time = int(input('Введите текущее время в часах:'))
print('Мы закрыты. Часы работы: с 10 до 24.')

1.5. Завершенная программа:
while input('Введите промокод:') != 'life':
    print('Этот промокод недействителен.')
print('Промокод принят.')

1.6. Завершенная программа:
promo = input('Введите промокод:')
while promo != 'life' and promo != 'health':
    promo = input('Этот промокод недействителен. Попробуйте снова:')
print('Промокод принят.')

1.7. Текст программы сбора отзывов:
text = input('Введите ваш отзыв:')
while text != 'off':
    print('Спасибо, ваш отзыв принят!')
    text = input('Введите ваш отзыв:')

1.9. Текст программы (автоподсчет суммы покупок):
price = int(input('Стоимость товара (0 - покупок больше нет):'))
cost = price
while price != 0:
    price = int(input('Стоимость товара (0 - покупок больше нет):'))
    cost += price           
print('Стоимость всех покупок: ' + str(cost))

Доп задание 1.1.


Доп задание 1.2
total = int(input('Введите стоимость покупок:'))
while total != 0:
    print('К оплате: ' + str(total * 0.9))
    total = int(input('Введите стоимость покупок:'))


Доп задание 1.3
text = input('Введите текст бегущей строки:')
while len(text) > 0:
    print(text[0])
    text = text[1:]


Задание 2. «Магазин: рекомендация товаров 2»

2.3.  Завершенная программа:
#Первые 3 покупателя получают скидку
count = 0
while count < 3:
    card = input('Введите номер карты:')
    print('Поздравляем! Вы получили скидку 10%.')
    count += 1
print('Скидки закончились.')

2.4. Программа:
#Подсчёт категорий товаров
category = input('Категория (end - завершить):')
count = 0
while category != 'end':
    count += 1
    category = input('Категория (end - завершить):')
print('Всего категорий товаров: ' + str(count))



2.5. Программа:
	attempts = 0
promo = ''
while attempts < 3 and promo != 'fresh':
   promo = input('Введите промокод:')
   attempts += 1
if promo == 'fresh':
   print('Принято с попытки №', attempts)


2.6. Программа:
#автомат для выдачи талонов


code = input('Введите 0 - получить талон, 1 - выключить аппарат:')
number = 0
while code != '1':
    if code == '0':
        number += 1
        print('талон номер ' + str(number))
    code = input('Введите 0 - получить талон, 1 - выключить аппарат:')


Доп задание. 2.1:
total = int(input('Введите сумму:'))
while total % 2 == 0:
    total = total / 2
print('К оплате: ' + str(total))


Доп задание 2.2:
n = int(input('Введите высоту:'))
i = 0
while i < n:
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    i += 1


Дополнительное задание. «Магазин: доп задание»

1.3. Код программы без ошибок:
category = input('Категория (stop - завершить):')
while category != 'stop':
    if category == 'мясные изделия':
        print('Скидка 10%.')
    elif category == 'напитки':
        print('Скидка 30%.')
    else:
        print('Скидок нет.')
    category = input('Введите категорию продуктов:')


1.4. Код программы:
category = input('Категория (off - завершить):')
while category != 'off':
    cost = int(input('Сумма:'))
    if category == 'молочные продукты':
        print('Скидка 10%. К оплате: ' + str(cost * 0.9))
    elif category == 'выпечка':
        print('Скидка 30%. К оплате: ' + str(cost * 0.7))
    else:
        print('К оплате: ' + str(cost))
    category = input('Введите категорию продуктов:')
print('Касса закрыта.')
