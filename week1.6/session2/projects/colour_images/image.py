import copy


class ImageError(Exception):
    pass


class Image:
    @classmethod
    def create(cls, width, height, value=0, maximum=255):
        image = cls()
        image.create_pixels(width, height, value, maximum)
        return image

    @classmethod
    def read(cls, filename):
        image = cls()
        image.read_pnm(filename)
        return image

    def read_pnm(self, filename):
        with open(filename, "rt") as infile:
            magic = infile.readline().strip()
            if magic not in ("P2", "P3"):
                raise ImageError("unrecognized magic number")
            self.magic_number = magic
            line = infile.readline().strip()
            if line.startswith("#"):
                line = infile.readline().strip()
            self.width, self.height = (int(part) for part in line.split())
            self.max_value = int(infile.readline().strip())
            values = [int(value) for value in infile.read().split()]

        if magic == "P2":
            if len(values) != self.width * self.height:
                raise ImageError("number of pixels doesn't match image dimensions")
        else:
            if len(values) != self.width * self.height * 3:
                raise ImageError("number of pixel components doesn't match dimensions")
            values = [
                tuple(values[index:index + 3])
                for index in range(0, len(values), 3)
            ]

        self.pixels = values
        if any(
            component < 0 or component > self.max_value
            for pixel in values
            for component in (pixel if isinstance(pixel, tuple) else (pixel,))
        ):
            raise ImageError("pixel value outside allowed range")

    def create_pixels(self, width, height, value=0, maximum=255):
        if width < 1 or height < 1:
            raise ImageError("image dimensions must be positive")
        self.width = width
        self.height = height
        self.max_value = maximum
        self.pixels = [copy.deepcopy(value) for _ in range(width * height)]

    def __getitem__(self, index):
        return self.pixels[index]

    def __setitem__(self, index, value):
        self.pixels[index] = value

    def get(self, row, col):
        return self.pixels[row * self.width + col]

    def set(self, row, col, value):
        self.pixels[row * self.width + col] = value

    def copy(self):
        return copy.deepcopy(self)

    def write_pnm(self, filename):
        with open(filename, "wt") as outfile:
            print(self.magic_number, file=outfile)
            print(self.width, self.height, file=outfile)
            print(self.max_value, file=outfile)
            for row in range(self.height):
                start = row * self.width
                for pixel in self.pixels[start:start + self.width]:
                    if isinstance(pixel, tuple):
                        print(*pixel, end=" ", file=outfile)
                    else:
                        print(f"{pixel:4d}", end=" ", file=outfile)
                print(file=outfile)

    def write_pgm(self, filename):
        self.write_pnm(filename)

    def write_ppm(self, filename):
        self.write_pnm(filename)


class GreyImage(Image):
    magic_number = "P2"

    def create_pixels(self, width, height, value=0, maximum=255):
        super().create_pixels(width, height, value, maximum)
        self.magic_number = "P2"


class ColourImage(Image):
    magic_number = "P3"

    @classmethod
    def create(cls, width, height, value=(0, 0, 0), maximum=255):
        return super().create(width, height, value, maximum)

    def create_pixels(self, width, height, value=(0, 0, 0), maximum=255):
        super().create_pixels(width, height, value, maximum)
        self.magic_number = "P3"
