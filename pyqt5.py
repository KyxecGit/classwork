from PyQt5.QtWidgets import (
    QApplication,QWidget, QLabel,
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

def you_lose():
    result = QMessageBox()
    result.setText('Поздравляем вы дебил')
    result.exec()

def you_win():
    result = QMessageBox()
    result.setText('Поздравляем вы не дебил')
    result.exec()

answer1.clicked.connect(you_lose)
answer2.clicked.connect(you_lose)
answer3.clicked.connect(you_lose)
answer4.clicked.connect(you_win)

win.show()
app.exec()
