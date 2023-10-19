import pandas as pd
df = pd.read_csv('GoogleApps.csv')


# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
temp = df['Category'].value_counts()
print(temp['BUSINESS'])


# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
temp = df['Content Rating'].value_counts()
print('Соотношение:', temp['Teen'] / temp['Everyone 10+'])


# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
# Ответ запиши с точностью до сотых.
temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])


# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(temp['Paid'] - temp['Free'])


# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
temp = df.groupby(by = 'Category')['Size'].agg(['min', 'max'])


# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
