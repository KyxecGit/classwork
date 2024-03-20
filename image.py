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
