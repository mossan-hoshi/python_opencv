from src.sample import path_through_image, image_process_sample
from pathlib import Path
import cv2
import numpy as np


def test_path_through_image():
    # set arguments
    base_dir_path = Path.cwd()
    in_file_path = base_dir_path / "data/sample.jpg"
    exp_file_path = in_file_path  # same as input image

    # read images
    in_image = cv2.imread(str(in_file_path))
    exp_image = cv2.imread(str(exp_file_path))

    result_image = path_through_image(in_image, None)

    assert np.array_equal(result_image, exp_image)


def test_image_process_sample():
    # set arguments
    base_dir_path = Path.cwd()
    in_file_path = base_dir_path / "data/sample.jpg"
    exp_file_path = base_dir_path / "tests/exp/image_process_sample.png"

    # read images
    in_image = cv2.imread(str(in_file_path))
    exp_image = cv2.imread(str(exp_file_path))

    result_image = image_process_sample(in_image, None)

    assert np.array_equal(result_image, exp_image)
