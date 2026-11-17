import sys

from image import Image
from lookup_tables import InvertLookupTable, SquareRootLookupTable


def main():
    if len(sys.argv) != 4:
        print("Usage: python apply_lookup.py <input.pgm> <invert|sqrt> <output.pgm>")
        return 1

    if sys.argv[2] == "invert":
        table = InvertLookupTable()
    elif sys.argv[2] == "sqrt":
        table = SquareRootLookupTable()
    else:
        print("Lookup type must be 'invert' or 'sqrt'")
        return 1

    image = Image.read(sys.argv[1])
    table.apply(image).write_pgm(sys.argv[3])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
