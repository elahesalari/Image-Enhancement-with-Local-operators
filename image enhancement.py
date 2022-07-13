import numpy as np
import cv2
import os
from skimage import io
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def read_image():
    image = []
    for filename in os.listdir('images'):
        img = io.imread(os.path.join('images', filename))
        image.append(img)

    return image


def enhancement(img):
    fig = plt.figure()
    fig.set_size_inches(4,10)
    spec = gridspec.GridSpec(ncols=2, nrows=10, figure=fig)

    gama = [1.9, 1.8, 1.8, 0.4, 0.5, 0.6, 3, 0.4,0.3,2]
    power_image = []
    for i in range(10):
        power_image.append(np.array(255 * (img[i] / 255) ** gama[i], dtype='uint8'))
        ax1 = fig.add_subplot(spec[i, 0])
        ax2 = fig.add_subplot(spec[i, 1])
        ax1.set_title('Original image',fontsize=5)
        ax2.set_title(f'Enhance image, gamma :{gama[i]}',fontsize=5)
        ax1.imshow(img[i],cmap='gray')
        ax2.imshow(power_image[i],cmap='gray')

        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])

    plt.tight_layout()
    plt.savefig('enhance images.jpg')
    plt.show()


if __name__ == '__main__':
    img = read_image()
    enhancement(img)
