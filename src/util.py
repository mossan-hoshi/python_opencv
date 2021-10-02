import cv2
from pathlib import Path
import argparse


def process_images_and_save(
    in_dir_path: Path,
    in_suffix: str,
    process_function: any,
    args: argparse.Namespace,
    out_dir_path: Path,
    out_suffix: str,
):

    # create output folder
    if not out_dir_path.exists():
        out_dir_path.mkdir(parents=True)

    # "read -> process -> save" image files
    for in_file_path in in_dir_path.glob(f"*{in_suffix}"):
        # read
        image = cv2.imread(str(in_file_path))

        # process
        image = process_function(image, args)

        # save
        out_file_path = out_dir_path / (in_file_path.stem + out_suffix)
        cv2.imwrite(str(out_file_path), image)

        print(f"[{in_file_path.name}] process done" + " " * 30, end="")
