from image import Image


def blur(image):
    """Return a 3x3 mean-blurred copy, preserving edge pixels."""
    result = image.copy()

    for row in range(1, image.height - 1):
        for col in range(1, image.width - 1):
            total = 0
            for offset_row in (-1, 0, 1):
                for offset_col in (-1, 0, 1):
                    total += image.get(row + offset_row, col + offset_col)
            result.set(row, col, total // 9)

    return result
