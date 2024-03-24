from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout


app = QApplication([])

'''Интерфейс приложения'''
#параметры окна приложения
win = QWidget()
win.setWindowTitle('Image Editor')
win.resize(800, 500)

#виджеты окна приложения
button_folder = QPushButton('Папка') 
list_images = QListWidget()


image_label = QLabel('Картинка')
button_left = QPushButton('Лево') 
button_right = QPushButton('Право') 
button_mirror = QPushButton('Зеркало') 
button_rezcost = QPushButton('Резкость') 
button_gray = QPushButton('Ч\Б') 


#расположение виджетов по лэйаутам
layout_main = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
row_1 = QHBoxLayout()

row_1.addWidget(button_left)
row_1.addWidget(button_right)
row_1.addWidget(button_mirror)
row_1.addWidget(button_rezcost)
row_1.addWidget(button_gray)

col_1.addWidget(button_folder)
col_1.addWidget(list_images)

col_2.addWidget(image_label)
col_2.addLayout(row_1)

layout_main.addLayout(col_1)
layout_main.addLayout(col_2)

win.setLayout(layout_main)
'''Функционал приложения'''


#запуск приложения 
win.show()
app.exec()
