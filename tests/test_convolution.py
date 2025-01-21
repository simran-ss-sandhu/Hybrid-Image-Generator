import unittest
import numpy as np
from PIL import Image, ImageOps
import os
from src.convolution import convolve


class TestConvolution(unittest.TestCase):
    def test_padding(self):
        img = Image.open(os.path.join('..', 'data', 'dog.bmp'))
        kernel = np.ones(shape=(3, 3))
        np_img = np.array(img)
        self.assertEqual(convolve(np_img, kernel).shape, np_img.shape)

    def test_padding_grayscale(self):
        img = Image.open(os.path.join('..', 'data', 'dog.bmp'))
        img = ImageOps.grayscale(img)
        kernel = np.ones(shape=(3, 3))
        np_img = np.array(img)
        self.assertEqual(convolve(np_img, kernel).shape, np_img.shape)

    def test_no_padding_needed(self):
        img = Image.open(os.path.join('..', 'data', 'dog.bmp'))
        img = img.resize(size=(300, 300))
        kernel = np.ones(shape=(3, 3))
        np_img = np.array(img)
        self.assertEqual(convolve(np_img, kernel).shape, np_img.shape)

    def test_non_square_kernel1(self):
        img = Image.open(os.path.join('..', 'data', 'dog.bmp'))
        kernel = np.ones(shape=(3, 5))
        np_img = np.array(img)
        self.assertEqual(convolve(np_img, kernel).shape, np_img.shape)

    def test_non_square_kernel2(self):
        img = Image.open(os.path.join('..', 'data', 'dog.bmp'))
        kernel = np.ones(shape=(5, 3))
        np_img = np.array(img)
        self.assertEqual(convolve(np_img, kernel).shape, np_img.shape)


if __name__ == '__main__':
    unittest.main()
