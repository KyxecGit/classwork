from PIL import Image, ImageFilter
#открой файл с оригиналом картинки
with Image.open('файл') as original:
    #сделай оригинал изображения чёрно-белым
    gray = original.convert('L')
    #сделай оригинал изображения размытым
    blur = gray.filter(ImageFilter.BLUR)
    #поверни оригинал изображения на 180 градусов
    perevorot = blur.transpose(Image.ROTATE_180)
    #сохранение
    perevorot.save('norm.jpg')
    #вывод изображения
    perevorot.show()




#подключи нужные модули PIL
from PIL import Image
from PIL import ImageFilter

#создай класс ImageEditor
class ImageEditor():
    #создай конструктор класса
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []
    #создай метод "открыть и показать оригинал"
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не найден')
        self.original.show()
        
    #создай методы для редактирования оригинала
    def zerkalo(self):
        rotate = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotate)
        filename = self.filename.split('.')
        new_filename = filename[0] + str(len(self.changed)) + '.jpg'
        rotate.save(new_filename)

    def crop(self,top,right,bottom,left):
        box = (top,right,bottom,left)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        filename = self.filename.split('.')
        new_filename = filename[0] + str(len(self.changed)) + '.jpg'
        cropped.save(new_filename)

#создай объект класса ImageEditor с данными картинки-оригинала
image1 = ImageEditor('koala.jpg')
image1.open()

image1.zerkalo()
image1.crop(250,100,600,400)



#отредактируй изображение и сохрани результат
