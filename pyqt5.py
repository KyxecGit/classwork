from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QGroupBox, QLabel,
    QRadioButton, QPushButton)

app = QApplication([])

win = QWidget()
win.setWindowTitle('Викторина')

# Интерфейс
question = QLabel('Ты кто по жизни?')
button = QPushButton('Ответить')
# Размещение
main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment = Qt.AlignHCenter)
main_layout.addWidget(button)
win.setLayout(main_layout)
# Запуск
win.show()
app.exec()
