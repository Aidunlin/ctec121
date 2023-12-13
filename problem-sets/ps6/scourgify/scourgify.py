# PS-6 Scourgify
# Aidan Linerud

import csv
import sys


def main():
    # Gets input and output file paths from command-line arguments,
    # or exits the program if there are more or less than two arguments
    match sys.argv:
        # Matches two specified arguments (the input and output files)
        case [_, inpath, outpath]:
            pass

        # Matches less than two specified arguments
        case [_] | [_, _]:
            sys.exit("Too few command-line arguments")

        # Matches any other case (i.e. more than two specified arguments)
        case _:
            sys.exit("Too many command-line arguments")

    # Tries to open the input file, exiting if it could not
    try:
        infile = open(inpath)
    except OSError:
        sys.exit(f"Could not read {inpath}")

    # Creates a CSV reader for the input file
    data = csv.reader(infile, delimiter=",", quotechar='"')
    # Advances past the header row in the input file
    next(data)

    # Tries to create an output file, exiting if it could not
    try:
        outfile = open(outpath, "w", newline="")
    except OSError:
        sys.exit(f"Could not create {outpath}")

    # Creates a CSV writer for the output file
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

    # Writes the header row to the output file
    writer.writeheader()

    # Converts each row in the input file to rows in the output file
    # by splitting each "name" value into separate "first" and "last" values
    for row in data:
        # First, matches the whole input row, which must be "name" and "house"
        # (or exits the program)
        match row:
            case [name, house]:
                pass
            case _:
                sys.exit("Row has invalid format")

        # Then, inside name, splits up first/last name
        # (or exits if it's not the right format)
        match name.split(", "):
            case [last, first]:
                pass
            case _:
                sys.exit("Row name has invalid format")

        # Finally, creates a dictionary for this row, and writes it to the output file
        row_data = {"first": first, "last": last, "house": house}
        writer.writerow(row_data)

    # Closes the input and output files
    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
