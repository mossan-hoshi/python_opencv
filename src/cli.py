"""Command line interface module for OpenCV-based python environment sample repository.
"""

import argparse
from pathlib import Path
from util import process_images_and_save
from sample import path_through_image
from sample import image_process_sample
from setting import ProcessMode


def parseArgs():
    parser = argparse.ArgumentParser(description="python image processing program")

    parser.add_argument(
        "--in_dir_path",
        type=str,
        default="data/sample.jpg",
        help="input image directory path",
    )
    parser.add_argument(
        "--in_suffix", type=str, default=".png", help="input image file extension"
    )

    parser.add_argument(
        "--out_dir_path", type=str, default="out/", help="output image directory path"
    )

    parser.add_argument(
        "--out_suffix", type=str, default=".png", help="output image file extension"
    )

    parser.add_argument(
        "--process_mode",
        type=int,
        default=1,
        help="Image processing mode (compliant with ProcessMode)",
    )

    args = parser.parse_args()

    # convert string argument to Path
    args.in_dir_path = Path(args.in_dir_path)
    args.out_dir_path = Path(args.out_dir_path)

    return args


def main():
    args = parseArgs()

    process_function = (
        path_through_image
        if args.process_mode == ProcessMode.PATH_THROUGH
        else image_process_sample
        if args.process_mode == ProcessMode.SAMPLE
        else None
    )

    process_images_and_save(
        in_dir_path=args.in_dir_path,
        in_suffix=args.in_suffix,
        args=args,
        process_function=process_function,
        out_dir_path=args.out_dir_path,
        out_suffix=args.out_suffix,
    )


if __name__ == "__main__":
    main()
