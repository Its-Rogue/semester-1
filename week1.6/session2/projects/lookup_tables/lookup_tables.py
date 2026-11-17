import math


class LookupTable:
    def __init__(self, values):
        if len(values) != 256:
            raise ValueError("a lookup table must contain 256 values")
        self.values = list(values)

    def display(self):
        for index, value in enumerate(self.values):
            print(f"{index:3d} -> {value:3d}")

    def apply(self, image):
        result = image.copy()
        for index in range(image.width * image.height):
            result[index] = self.values[result[index]]
        return result

    def apply_in_place(self, image):
        for index in range(image.width * image.height):
            image[index] = self.values[image[index]]


class IdentityLookupTable(LookupTable):
    def __init__(self):
        super().__init__(range(256))


class InvertLookupTable(LookupTable):
    def __init__(self):
        super().__init__(tuple(255 - value for value in range(256)))


class SquareRootLookupTable(LookupTable):
    def __init__(self):
        scale = 255 / math.sqrt(255)
        super().__init__(tuple(
            min(255, round(math.sqrt(value) * scale))
            for value in range(256)
        ))
