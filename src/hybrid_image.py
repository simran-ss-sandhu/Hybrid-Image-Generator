import math
import numpy as np
import logging
from PIL import Image
from convolution import convolve


logging.basicConfig(level=logging.INFO, format="|%(asctime)s|%(name)s|%(levelname)s| %(message)s")


def create_hybrid_image(near_img_path: str, low_sigma: float, far_img_path: str, high_sigma: float,
                        output_img_path: str) -> np.ndarray:
    """
    Create hybrid images by combining a low-pass and high-pass filtered pair.

    :param output_img_path: the path to save the hybrid image to
    :param near_img_path: the image path to low-pass filter
    :param low_sigma: the standard deviation of the Gaussian used for low-pass filtering lowImage
    :param far_img_path: the image path to high-pass filter
    :param high_sigma: the standard deviation of the Gaussian used for low-pass filtering highImage before subtraction
        to create the high-pass filtered image
    """

    # load images
    near_img = Image.open(near_img_path)
    far_img = Image.open(far_img_path)

    # make images the same size
    near_img = near_img.resize(size=(350, 350))
    far_img = far_img.resize(size=(350, 350))

    # convert to numpy array to prepare for processing
    far_img = np.array(far_img)
    near_img = np.array(near_img)

    logging.info("Applying low-pass filter")
    low = convolve(far_img, __create_gaussian_kernel(low_sigma))

    logging.info("Applying high-pass filter")
    high = near_img - convolve(near_img, __create_gaussian_kernel(high_sigma))

    hybrid_img_arr = low + high  # create hybrid image
    hybrid_img_arr = np.clip(hybrid_img_arr, 0, 255).astype(np.uint8)  # remove out of range pixels
    hybrid_img = Image.fromarray(hybrid_img_arr)  # convert to Image object
    hybrid_img.save(output_img_path)  # save to file
    logging.info(f"Saved Hybrid image to \'{output_img_path}\'")

    return hybrid_img_arr


def __create_gaussian_kernel(sigma: float) -> np.ndarray:
    """
    Use this function to create a 2D gaussian kernel with standard deviation sigma.
    The kernel values should sum to 1.0, and the size should be floor(8*sigma+1)
    or floor(8*sigma+1)+1 (whichever is odd) as per the assignment specification.
    """

    size = int(8.0 * sigma + 1.0)

    # ensures size is odd
    if size % 2 == 0:
        size += 1

    sigma_squared = sigma ** 2

    kernel = np.zeros(shape=(size, size), dtype=np.float64)

    half_size = size // 2

    for row, y in enumerate(range(-half_size, half_size)):
        for col, x in enumerate(range(-half_size, half_size)):
            kernel[row, col] = math.exp(-(x ** 2 + y ** 2) / (2 * sigma_squared)) / (2 * np.pi * sigma_squared)

    return kernel
