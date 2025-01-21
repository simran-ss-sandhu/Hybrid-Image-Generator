import matplotlib.pyplot as plt
import numpy as np


def __plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.show()


def __plot_images(img1: np.array, img2: np.array):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1)
    ax[1].imshow(img2)
    plt.show()


def showcase_image(img: np.array):
    _, ax = plt.subplots(1, 6, figsize=(15, 10), width_ratios=[8, 6, 4, 2, 1.5, 1])
    for x in range(6):
        ax[x].imshow(img)
        ax[x].set_xticks([])
        ax[x].set_yticks([])
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()
