import os
import argparse

import cv2
import numpy as np


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="")
    arg_parser.add_argument(
        "dir",
        type=str,
        help="directory to crop"
    )
    args = arg_parser.parse_args()
    assert os.path.isdir(args.dir)
    for p in os.listdir(args.dir):
        try:
            img = cv2.imread(os.path.join(args.dir, p)) # Read in the image and convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            continue
        coords = cv2.findNonZero((gray != 255).astype(np.uint8))
        x, y, w, h = cv2.boundingRect(coords)
        cropped = img[y:y+h, x:x+w, ...]
        if not os.path.isdir(os.path.join(args.dir, "cropped")):
            os.mkdir(os.path.join(args.dir, "cropped"))
        cv2.imwrite(os.path.join(args.dir, "cropped", p), cropped)
        print("Processed {}".format(os.path.join(args.dir, p)))
