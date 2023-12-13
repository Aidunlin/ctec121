# shirt.py
# Aidan Linerud

# For adding the shirt image on top of an input image
from PIL import Image, ImageOps

# For reading command-line arguments from the user,
# and exiting the program when an error occurs
import sys

# For getting the file extensions of input/output paths
import os


def main():
    # Exits the program if the user specified less than 2 args
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Exits the program if the user specified more than 2 args
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Validates file arguments if the user specified exactly 2 args
    if len(sys.argv) == 3:
        # Splits each file argument into a list that contains the name and extension
        file1 = os.path.splitext(sys.argv[1])
        file2 = os.path.splitext(sys.argv[2])

        # Exits the program if the first file isn't a JPG or PNG
        if file1[1].lower() != ".jpg" and file1[1].lower() != ".png":
            sys.exit("Invalid input")

        # Exits the program if the second file isn't a JPG or PNG
        if file2[1].lower() != ".jpg" and file2[1].lower() != ".png":
            sys.exit("Invalid input")

        # Exits the program if the two files don't have the same extension
        if file1[1].lower() != file2[1].lower():
            sys.exit("Files must have the same extension")

    # Gets shirt and input images, exiting if the input file doesn't exist
    shirt = Image.open("shirt.png")
    try:
        before = Image.open(sys.argv[1])
    except IOError:
        sys.exit("Input file does not exist")

    # Resizes and crops the input image to work with the shirt image.
    #
    # By default, ImageOps.fit() will equally cut the edges to fit the image,
    # and use bicubic sampling to upscale the image if it is smaller than 600x600.
    # So, we don't need to specify this method's default arguments
    # (method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    before = ImageOps.fit(before, (600, 600))

    # Pastes the shirt onto the input image, and saves the results to the output file argument.
    #
    # To maintain the shirt image's transparency and NOT overwrite the entire input image,
    # pass the shirt image again as a mask, which will ensure that transparent pixels from
    # the shirt image won't overwrite the rest of the input image as black/white pixels.
    before.paste(shirt, shirt)
    before.save(sys.argv[2])

    # Exits the program
    sys.exit(0)


if __name__ == "__main__":
    main()
