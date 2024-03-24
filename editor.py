import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel,QPushButton,QListWidget,
    QHBoxLayout, QVBoxLayout,
    QFileDialog)

# Интерфейс
app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Фотошоп на минималках')

btn_papka = QPushButton('Папка')
files = QListWidget()

image = QLabel('Картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_zerkalo = QPushButton('Зеркало')
btn_rezcost = QPushButton('Резкость')
btn_gray = QPushButton('Ч/Б')

# Размещение виджетов
main_layout = QHBoxLayout()
h1 = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()

h1.addWidget(btn_left)
h1.addWidget(btn_right)
h1.addWidget(btn_zerkalo)
h1.addWidget(btn_rezcost)
h1.addWidget(btn_gray)

v1.addWidget(btn_papka)
v1.addWidget(files)

v2.addWidget(image)
v2.addLayout(h1)

main_layout.addLayout(v1)
main_layout.addLayout(v2)
win.setLayout(main_layout)

# Функционал

def ShowImages():
    workdir = QFileDialog().getExistingDirectory()
    all_files = os.listdir(workdir)

    image_files = []
    for filename in all_files:
        for extensions in ['.jpg','.png','jpeg']:
            if filename.endswith(extensions):
                image_files.append(filename)

    files.clear()
    files.addItems(image_files)

# Подписки
btn_papka.clicked.connect(ShowImages)

# Запуск
win.show()
app.exec()
