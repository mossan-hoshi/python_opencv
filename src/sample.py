import numpy as np


def path_through_image(image: np.array, args):
    return image


def image_process_sample(image: np.array, args):
    # Perform some appropriate image processing :)

    # convert image type to float
    original_image_type = image.dtype
    image = image.astype(np.float64)

    # draw zone plate
    # https://en.wikipedia.org/wiki/Zone_plate
    y_center = image.shape[0] / 2
    x_center = image.shape[1] / 2
    y, x = np.indices(image.shape[:2])
    distance = (y[None, :, :] - y_center) ** 2 + (x[None, :, :] - x_center) ** 2
    zone_plate = (1 + np.cos(distance / 100.0)) / 2.0
    zone_plate = np.reshape(zone_plate, zone_plate.shape[1:])

    # blend
    for c in range(image.shape[2]):
        image[..., c] *= zone_plate

    result_image = image.astype(original_image_type)

    return result_image
