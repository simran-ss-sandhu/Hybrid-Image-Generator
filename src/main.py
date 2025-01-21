import argparse
import logging
import os
from PIL import Image
from hybrid_image import create_hybrid_image
from visualiser import showcase_image


logging.basicConfig(level=logging.INFO, format="|%(asctime)s|%(name)s|%(levelname)s| %(message)s")


LOW_SIGMA = 5  # higher number means weaker far image
HIGH_SIGMA = 15  # higher number means stronger near image


def __validate_input_arg(img_path) -> None:
    """
    Checks if the file exists and if it's an image

    :param img_path: path of the input image
    """

    # check if the file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file exists at \'{img_path}\'")

    # checks if the file is an image
    with Image.open(img_path) as img:
        img.verify()


def __validate_output_arg(img_path) -> None:
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    _, ext = os.path.splitext(img_path)
    if ext not in image_extensions:
        raise TypeError(f"Output path \'{img_path}\' is not of an image")


def __validate_sigma_arg(sigma):
    if sigma < 0:
        raise ValueError("Sigma values must be >= 0")


def main():

    # tool arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, nargs=2, required=True,
                        help='Input file paths (near_img_path far_img_path)')
    parser.add_argument('--output', type=str, required=True,
                        help='Output image path for the generated Hybrid image')
    parser.add_argument('--sigma', type=int, nargs=2, required=False,
                        help='Sigma values (low_boundary high_boundary)')
    parser.add_argument('--visualiser', action='store_true', help='Output Visualiser', required=False)

    args = parser.parse_args()

    # collect and validate input image path args
    near_img_path, far_img_path = args.input
    logging.info("Validating input args")
    __validate_input_arg(near_img_path)
    __validate_output_arg(far_img_path)

    # collect and validate output image path arg
    output_img_path = args.output
    logging.info("Validating output arg")
    __validate_output_arg(output_img_path)

    # collect and validate sigma args
    if args.sigma:
        low_boundary, high_boundary = args.sigma
        logging.info("Validating sigma args")
        __validate_sigma_arg(low_boundary)
        __validate_sigma_arg(high_boundary)
    else:
        logging.info("No sigma args specified. Using default values")
        low_boundary = LOW_SIGMA
        high_boundary = HIGH_SIGMA

    logging.info(
        "Args: ["
        + f"near_img_path=\'{near_img_path}\', "
        + f"far_img_path=\'{far_img_path}\', "
        + f"output_img_path=\'{output_img_path}\', "
        + f"low_boundary={low_boundary}, "
        + f"high_boundary={high_boundary}, "
        + f"visualiser={args.visualiser}]"
    )

    logging.info("Creating Hybrid image")
    hybrid_img = create_hybrid_image(near_img_path, low_boundary, far_img_path, high_boundary, output_img_path)

    if args.visualiser:
        logging.info("Creating Visualiser")
        showcase_image(hybrid_img)

    logging.info("Done")


if __name__ == '__main__':
    main()
