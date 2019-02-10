import os
import sys
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class Viewer(object):
    def get_float_color(color):
        assert len(color) == 3, "Цвет должен быть массивом длины 3"
        R = color[0]
        G = color[1]
        B = color[2]
        assert 0 <= R <= 255 and 0 <= G <= 255 and 0 <= B <= 255
        color_zero_one = [color[0]/255, color[1]/255, color[2]/255]
        return color_zero_one

    def img_print(Number):
        im = Image.open(str(Number).join(('Google Colab/', '.jpg')))
        im.show()

    def draw_circle(color):
        plt.figure(figsize=(2, 2))
        plt.axis('off')
        plt.scatter([0], [0], s=10000, color=color)
        plt.show()

    def mean_color(picture):
        AVG = [0, 0, 0]
        for columns in np.asarray(picture):
            for color in columns:
                AVG[0] += color[0]
                AVG[1] += color[1]
                AVG[2] += color[2]

        Size = np.asarray(picture).shape[0] * np.asarray(picture).shape[1]
        AVG[0] = AVG[0] / Size
        AVG[1] = AVG[1] / Size
        AVG[2] = AVG[2] / Size
        return AVG

    def get_cropped(i, size):
        im = Image.open(str(i).join(('Google Colab/', '.jpg')))
        left, top, right, bottom = 0, 0, size[0], size[1]
        cropped = im.crop((left, top, right, bottom))
        cropped.show()

    def get_resized(i, size):
        '''im = Image.open(str(i).join(('Google Colab/', '.jpg')))
        image_array = np.asarray(im)
        python_array = []
        for i in xrange(0,100):
            python_array.append(0)

        image_resized = np.array(python_array)
        width, height = im.size # Размер картинки
        pixel_x = int(width / size[0])
        pixel_y = int(height / size[1])
        for line in range(size[1]):
            for column in range(size[0]):
                image_resized[line, column] = mean_color() # image_array[]'''

    def dist(color1, color2):
        dis1 = (color1[0]-color2[0]) ** 2
        dis2 = (color1[1]-color2[1]) ** 2
        dis3 = (color1[2]-color2[2]) ** 2
        d = (dis1 + dis2 + dis3) ** .5
        return d

if __name__ == "__main__":
    # Viewer.img_print(2)
    # Viewer.get_cropped(1, [50, 50])
    # Viewer.get_resized(2, [640, 330])
    sys.exit()
