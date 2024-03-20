from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QGroupBox, QLabel,
    QRadioButton, QPushButton)

#Интерфейс
app = QApplication([])
win = QWidget()

# Запуск
win.show()
app.exec()
