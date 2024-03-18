from PyQt5.QtWidgets import (
    QApplication,QWidget, QPushButton, QLabel,
    QMessageBox,QRadioButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
win.resize(200,200)
win.setWindowTitle('Тест на дебилизм')

text = QLabel('Сколько будет 2 + 2')

answer1 = QRadioButton('5')
answer2 = QRadioButton('пять')
answer3 = QRadioButton('низнаю')
answer4 = QRadioButton('4')

main = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

main.addWidget(text, alignment = Qt.AlignCenter)

h1.addWidget(answer1, alignment = Qt.AlignLeft)
h1.addWidget(answer2, alignment = Qt.AlignLeft)
h2.addWidget(answer3, alignment = Qt.AlignLeft)
h2.addWidget(answer4, alignment = Qt.AlignLeft)

main.addLayout(h1)
main.addLayout(h2)

win.setLayout(main)

win.show()
app.exec()
