"""Image manipulation utilities."""

__all__ = ["get_full_raster_image_path", "drag_pixels", "invert_image", "premultiplied_image"]


from typing import List

import numpy as np
from PIL import Image

from .. import config
from ..utils.file_ops import seek_full_path_from_defaults

def premultiplied_image(image: np.array, width, height) -> np.array:
    for i in range(width):
        for j in range(height):
            if image[i, j][3] != 0:
                R = int(round(255.0 * image[i, j][0] / image[i, j][3]))
                G = int(round(255.0 * image[i, j][1] / image[i, j][3]))
                B = int(round(255.0 * image[i, j][2] / image[i, j][3]))
                a = image[i, j][3]

                image[i, j] = (R, G, B, a)

    return image

def get_full_raster_image_path(image_file_name: str) -> str:
    return seek_full_path_from_defaults(
        image_file_name,
        default_dir=config.get_dir("assets_dir"),
        extensions=[".jpg", ".jpeg", ".png", ".gif", ".ico"],
    )


def drag_pixels(frames: List[np.array]) -> List[np.array]:
    curr = frames[0]
    new_frames = []
    for frame in frames:
        curr += (curr == 0) * np.array(frame)
        new_frames.append(np.array(curr))
    return new_frames


def invert_image(image: np.array) -> Image:
    arr = np.array(image)
    arr = (255 * np.ones(arr.shape)).astype(arr.dtype) - arr
    return Image.fromarray(arr)
