import pandas as pd 
# Шаг 1. Загрузка данных
df = pd.read_csv('titanic.csv')
# Шаг 2. Удаление ненужных столбцов
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)
# Шаг 3. Работа со столбцом портов
df['Embarked'].fillna('S', inplace = True)
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis = 1, inplace = True)
# Шаг 4. Работа со столбцом возраста
age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()
def fill_age(row):
   if pd.isnull(row['Age']):
       if row['Pclass'] == 1:
           return age_1
       if row['Pclass'] == 2:
           return age_2
       return age_3
   return row['Age']
df['Age'] = df.apply(fill_age, axis = 1)
# Шаг 5. Работа со столбцом пола
def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0
df['Sex'] = df['Sex'].apply(fill_sex)
