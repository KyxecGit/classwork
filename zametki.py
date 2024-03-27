import os
from PIL import Image
from PIL.ImageFilter import SHARPEN
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout)

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Фотошоп на минималках')

# СОЗДАНИЕ ВИДЖЕТОВ
btn_folder = QPushButton('Папка')
list_images = QListWidget()

label_image = QLabel('Картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Отзеркалить')
btn_hd = QPushButton('Резкость')
btn_gray = QPushButton('Ч\Б')
#РАЗМЕЩЕНИЕ ВИДЖЕТОВ

v1 = QVBoxLayout()
v1.addWidget(btn_folder)
v1.addWidget(list_images)

h1 = QHBoxLayout()
h1.addWidget(btn_left)
h1.addWidget(btn_right)
h1.addWidget(btn_mirror)
h1.addWidget(btn_hd)
h1.addWidget(btn_gray)

v2 = QVBoxLayout()
v2.addWidget(label_image)
v2.addLayout(h1)

main_layout = QHBoxLayout()
main_layout.addLayout(v1)
main_layout.addLayout(v2)

win.setLayout(main_layout)

#Функционал
workdir = ''

def show_images():
    global workdir
    workdir = QFileDialog().getExistingDirectory()
    filenames = os.listdir(workdir)
    list_images.clear()
    for file in filenames:
        for extension in ['.jpg','.jpeg','.png']:
            if file.endswith(extension):
                list_images.addItem(file)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = 'Mod/'

    def loadImage(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir,filename) 
        self.image = Image.open(fullname)

    def showImage(self,path):
        label_image.hide()
        image = QPixmap(path)
        w, h = label_image.width(), label_image.height()
        image = image.scaled(w,h, Qt.KeepAspectRatio)
        label_image.setPixmap(image)
        label_image.show()

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path,self.filename) 
        self.image.save(fullname)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(path)
    
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(path)
    
    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        path = os.path.join(workdir, self.save_dir, self.filename)
        print(path)
        self.showImage(path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(path)

def showChosenImage():
    if list_images.currentRow() >= 0:
        filename = list_images.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(os.path.join(workdir, workimage.filename))

#Подписки на события
workimage = ImageProcessor() 
list_images.currentRowChanged.connect(showChosenImage)

btn_folder.clicked.connect(show_images)
btn_gray.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_hd.clicked.connect(workimage.do_sharpen)
btn_mirror.clicked.connect(workimage.do_flip)

win.show()
app.exec()
