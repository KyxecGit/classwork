Задание 1. «Магазин: рекомендация товаров»
1.1. Правильные варианты ответов:


1.5. Программа после исправления ошибок:
sales = input('Желаете товары по акции?')
if sales == 'да':
   category = input('Введите категорию:')
   if category == 'сладости':
       print('Фруктовый мармелад за 200 рублей')
   else:
       print('Брусничный морс за 140 рублей')
else:
   print('Сообщите, если передумаете!')

1.6. Программа после исправления ошибок:
category = input('Категория в разделе "Прямо с грядки":')
if category == 'зелень':
   max_price = int(input('Максимальная цена:'))
   if max_price >= 100:
       print('Попробуйте салатные миксы')
   else:
       print('Попробуйте ассорти из лука и петрушки')
else:
   print('Как насчёт батата?')

1.7. Текст программы для печати хитов продаж:
answer = input('Желаете изучить хиты продаж?')
if answer == 'да':
   category = input('Интересующая категория:')
   if category == 'продукты':
       print('Молоко 1л, Печенье с изюмом, Персики')
   else:
       print('Стиральный порошок, Щётка для обуви')
else:
   print('Дайте знать, если передумаете!')

1.8. Текст программы для акции «1 = 3»:


Решение 1:
price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
#поиск наибольшей цены
if price1 >= price2:
   if price1 >= price3:
       print('Акция! К оплате за три товара:', price1)
   else:
       print('Акция! К оплате за три товара:', price3)
else:
   if price2 >= price3:
       print('Акция! К оплате за три товара:', price2)
   else:
       print('Акция! К оплате за три товара:', price3)


Решение 2 «Олимпиадное»:
price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
#поиск наибольшей цены
if price1 <= price2:
   price1 = price2
if price1 <= price3:
   price1 = price3
print('Акция! К оплате за три товара:', price1)

Доп задание 1.1.


Доп задание 1.2

price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
#проверка упорядоченности цен по возрастанию
total = price1 + price2 + price3
if price1 < price2 and price2 < price3:
  total = total/2
  print('Акция!')
#проверка упорядоченности цен по убыванию
if price1 > price2 and price2 > price3:
  total = total/3
  print('Акция!')
print('К оплате:', total)


Доп задание 1.3
category = input('Категория:')
if category == 'продукты':
   price = int(input('Цена:'))
   if price < 100:
       print('Попробуйте нашу выпечку!')
   if price >= 100 and price < 500:
       print('Как насчёт орехов в шоколаде?')
   if price >= 500:
       print('Попробуйте экзотические фрукты!')
else:
   print('Загляните в товары для дома!')


Задание 2. «Магазин: рекомендация товаров 2»

2.1. Верны следующие варианты ответов:


2.4. Программа после исправления ошибок:
category = input('Введите категорию:')
if category == 'хит продаж':
   print('Товар недели - виноград Киш-миш')
elif category == 'веган':
   print('Попробуйте спаржу с тофу!')
else:
   print('Как насчёт свиного шашлычка?')

2.5. Программа для назначения акции в «Счастливые часы»:
total = int(input('Сумма:'))
time = int(input('Текущее время (час):'))
if time >= 20 and time <= 22:
  total = total/2
  print('Акция! Итого к оплате:', total)
elif time >= 8 and time < 20:
  print('Итого к оплате:', total)
else:
  print('Магазин не работает!')


2.6. Программа поиска товаров для праздника
#поиск по категории "Праздник"
category = input('Введите подкатегорию:')
if category == 'еда':
   print('Вам пригодятся: торт, чипсы, газировка')
elif category == 'оформление':
   print('Вам пригодятся: свечи, шары')
else:
   print('Загляните в хиты продаж!')


Доп задание. 2.1:
answer = input('Желаете познакомиться с необычным ассортиментом?')
if answer == 'да':
   product = input('Введите вид товара:')
   if product == 'напиток':
       taste = input ('Введите вкус:')
       if taste == 'лимонный':
           print('Попробуйте лимонад Лайм-Кактус!')
       elif taste == 'яблочный':
           print('Попробуйте газировку Печёное яблоко')
       else:
           print('Попробуйте напиток Озорная ежевика')
   else:
       print('Попробуйте можжевеловый пирог!')
else:
   print('Жаль! Будем ждать вас')


Доп задание 2.2:
#прогнозирование покупателей
amount1 = int(input('Введите число покупателей за позавчера:'))
amount2 = int(input('Введите число покупателей за вчера:'))
if amount2 > amount1:
   amount3 = amount2 + (amount2 - amount1)
elif amount2 < amount1:
   amount3 = amount2 - (amount1 - amount2)
else:
   amount3 = amount2
print ('Сегодня магазин посетит:', amount3, 'человек')


Дополнительное задание. «Магазин: доп задание»
1.1. Верные варианты ответов:


1.3. Код программы без ошибок:
mood = input('Ваше настроение:')
if mood == 'весёлое':
   print('Попробуйте апельсиновый лимонад!')
elif mood == 'спокойное':
   print('Как насчёт ягодного чая?')
else:
   print('Вам понравится вишнёвый йогурт!')


1.4. Код программы:
answer = int(input('Оцените наш магазин от 1 до 5:'))
if answer == 5:
   print('Мы работаем ради вас!')
elif answer < 5 and answer >= 3:
   wish = input('Уточните, что вам не понравилось?')
   print('Спасибо за отзыв!')
else:
   print('Мы перезвоним вам, чтобы узнать подробности!')
