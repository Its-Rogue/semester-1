import sys

from filters import blur
from image import Image


def main():
    if len(sys.argv) != 3:
        print("Usage: python blur.py <input.pgm> <output.pgm>")
        return 1

    original = Image.read(sys.argv[1])
    result = blur(original)
    result.write_pgm(sys.argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
