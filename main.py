months = 'январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь'.split()
sales = input('Введите данные о доходах с января по декабрь').split()
sales = list(map(int, sales))
growth = []
fall = []
for i in range(1, len(sales)):
    if sales[i] > sales[i-1]:
        growth.append(months[i])
    if sales[i] < sales[i-1]:
        fall.append(months[i])
print('Месяцы роста доходов:', growth)
print('Месяцы снижения доходов:', fall)




data = dict() 
while input('Желаете посетить урок программирования (да/нет)?').lower() == 'да':
    topic = input('Введите тему урока')
    if topic in data:
        data[topic] += 1
    else:
        data[topic] = 1 
total_lessons = 0
for lesson in list(data.values()):
    total_lessons += lesson
total_topics = len(data)
print('Общее количество уроков:', total_lessons)
print('Рассмотрено тем:', total_topics)




start_year = int(input('Год начала учёта')) 
end_year = int(input('Год окончания учёта')) 
data = dict()
for year in range(start_year, end_year+1):
    data[year] = dict()
for year in range(start_year, end_year+1):
    while input('Желаете добавить тему в проекты ' + str(year) + ' года (да/нет)?') == 'да':
        topic = input('Введите тему') 'Криптовалюты'
        projects = list(map(int, input('Введите данные о количестве заявок (в строку через пробел)').split()))
        if topic in data[year]:
            data[year][topic] += projects
        else:
            data[year][topic] = projects 

projects = dict()
for year in data:
    for topic in data[year]:
        total = 0
        for amount in data[year][topic]:
            total += amount 70
        if topic in projects:
            projects[topic] += total
        else:
            projects[topic] = total

print('РЕЗУЛЬТАТЫ АНАЛИЗА:')
total = 0
for topic in projects:
    print(topic, '-', projects[topic], 'проектов.')
    total += projects[topic]
print('Общее количество проектов:', total)


n = int(input('Введите бюджет компании:')) 
x = int(input('Введите зарплату senior-разработчика:')) 
y = int(input('Введите зарплату middle-разработчика:')) 
z = int(input('Введите зарплату junior-разработчика:')) 

qual1 = n//x 
balance = n%x 
qual2 = balance//y 
balance = balance%y 
qual3 = balance//z 
balance = balance%z 

print('Количество senior-разработчиков',qual1)
print('Количество middle-разработчиков',qual2)
print('Количество junior-разработчиков',qual3)
print('Остаток средств после распределения',balance)
