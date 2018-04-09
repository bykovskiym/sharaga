import os
from PIL import Image
from matplotlib import pyplot as plt

class Colors:

    def __init__(self, eat, step, dir, kull=0, ifkull=True):
        # задаем начальные данные
        self.eat = eat
        self.step = step
        self.dir = dir
        self.kull = kull
        self.ifkull = ifkull
        self.txt = ''
        self.files = []
        self.givefiles()

    def rgb_to_cmyk(self, r, g, b, rgb_scale=255, cmyk_scale=100):

        if (r == 0) and (g == 0) and (b == 0):
            # black
            return 0, 0, 0, cmyk_scale

        # rgb [0,255] -> r'g'b'[0,1]
        R = r / float(rgb_scale)
        G = g / float(rgb_scale)
        B = b / float(rgb_scale)

        # extract cmyk [0,1]
        m = max(R, G, B)
        k = 1 - m
        c = (1 - R - k) / (1 - k)
        m = (1 - G - k) / (1 - k)
        y = (1 - B - k) / (1 - k)

        # rescale to the range [0,cmyk_scale]
        return int(c*cmyk_scale), int(m*cmyk_scale), int(y*cmyk_scale), int(k*cmyk_scale)

    def gcr(self, im, percentage=0):
        '''basic "Gray Component Replacement" function. Returns a CMYK image with
           percentage gray component removed from the CMY channels and put in the
           K channel, ie. for percentage=100, (41, 100, 255, 0) >> (0, 59, 214, 41)'''
        cmyk_im = im.convert('CMYK')
        if not percentage:
            return cmyk_im
        cmyk_im = cmyk_im.split()
        cmyk = []
        for i in range(4):
            cmyk.append(cmyk_im[i].load())
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                gray = min(cmyk[0][x,y], cmyk[1][x,y], cmyk[2][x,y]) * percentage / 100
                for i in range(3):
                    cmyk[i][x,y] = cmyk[i][x,y] - gray
                cmyk[3][x,y] = gray
        return Image.merge('CMYK', cmyk_im)

    def conv(self, image1):
        mass = [self.rgb_to_cmyk(pixel[0], pixel[1], pixel[2]) for pixel in iter(image1.getdata())]
        cmyk = self.gcr(image1)
        cmyk.putdata(mass)
        return cmyk

    def clean(self):
        i = 0
        for k in self.eat:
            self.eat[i][4] = 0
            i += 1

    def givefiles(self):
        self.files = os.listdir(self.dir)

    def calckull(self, image):
        width, height = image.size
        if (width >= height):
            self.kull = width * 10
        else:
            self.kull = height * 10

    def calceat(self):
        self.txt = ''
        for e in self.eat:
            if (e[4] > self.kull):
                self.txt += e[5] + ', '

    def calcpixels(self, pixel):
        i = 0
        for e in self.eat:
            if (e[0] - self.step < pixel[0] and pixel[0] < e[0] + self.step and
                            e[1] - self.step < pixel[1] and pixel[1] < e[1] + self.step and
                            e[2] - self.step < pixel[2] and pixel[2] < e[2] + self.step and
                            e[3] - self.step < pixel[3] and pixel[3] < e[3] + self.step):
                self.eat[i][4] += 1
                m = [0, 0, 0, 100]
                return m
            i += 1
        return False

    def justdo(self):

        for im in self.files:

            image = Image.open(self.dir + im)

            if(self.ifkull):
                self.calckull(image)

            image = self.conv(image)
            image.show()

            self.clean()

            i = 0

            imag = image.getdata()
            pixels = [[pixel[0], pixel[1], pixel[2], pixel[3]] for pixel in iter(imag)]

            for pixel in iter(imag):
                p = self.calcpixels(pixel)
                if(p):
                    pixels[i] = p
                i += 1

            print(self.eat)

            pix = [(pixel[0], pixel[1], pixel[2], pixel[3]) for pixel in iter(pixels)]

            self.calceat()

            image.putdata(pix)
            plt.title(self.txt)
            plt.imshow(image)
            plt.show()