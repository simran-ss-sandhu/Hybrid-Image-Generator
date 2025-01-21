import numpy as np


def convolve(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Convolve an image with a kernel assuming zero-padding of the image to handle the borders

    :param image: the image (either greyscale shape=(rows,cols) or colour shape=(rows,cols,channels))
    :param kernel: the kernel (shape=(kheight,kwidth); both dimensions odd)
    :returns the convolved image (of the same shape as the input image)
    """

    # flips kernel
    kernel = np.flip(kernel)

    # pads image
    padding_h = kernel.shape[0] // 2
    padding_w = kernel.shape[1] // 2
    padded_shape = (image.shape[0] + padding_h * 2, image.shape[1] + padding_w * 2) + image.shape[2:]
    padded_img = np.zeros(shape=tuple(padded_shape), dtype=np.int16)
    padded_img[padding_h:-padding_h, padding_w:-padding_w] = image

    convolved_img = np.zeros(shape=image.shape, dtype=np.int16)

    if len(image.shape) == 2:  # image is grayscale
        for i in range(convolved_img.shape[0]):
            for j in range(convolved_img.shape[1]):
                sub = padded_img[i:i + kernel.shape[0], j:j + kernel.shape[1]]
                convolved_img[i, j] = np.sum(np.multiply(sub, kernel))
        return convolved_img
    elif len(image.shape) == 3:  # image is coloured
        for i in range(convolved_img.shape[0]):
            for j in range(convolved_img.shape[1]):
                for k in range(convolved_img.shape[2]):
                    sub = padded_img[i:i + kernel.shape[0], j:j + kernel.shape[1], k]
                    convolved_img[i, j, k] = np.sum(np.multiply(sub, kernel))
        return convolved_img
