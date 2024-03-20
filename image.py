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
from PIL import Image, ImageFilter
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
            self.original = Image.open(self.filename).show()
        except:
            print('Файл не найден')

    #создай методы для редактирования оригинала
#создай объект класса ImageEditor с данными картинки-оригинала
image1 = ImageEditor('lion.jpg')
image1.open()

#отредактируй изображение и сохрани результат
