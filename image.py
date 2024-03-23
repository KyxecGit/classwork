from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = Image.open(filename)
        self.mod = []

    def gray(self):
        gray = self.original.convert('L')
        self.mod.append(gray)
        new_filename = self.filename.split('.') 
        new_filename = new_filename[0] + str(len(self.mod)) + '.jpg'
        gray.save(new_filename)

image1 = ImageEditor('gitler.jpg')
image1.gray()

