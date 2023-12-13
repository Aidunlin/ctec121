# PS-6 Pizza Py
# Aidan Linerud

import csv
import io
import sys
import tabulate


# Returns a python file path from command-line arguments,
# or exits the program if there's too many/few arguments
# (or if the file is not a CSV file)
def get_path_from_args() -> str:
    match sys.argv:
        # Only allowed case
        # The wildcard "_" skips the first argument (which is always the current running program)
        case [_, path]:
            if not path.endswith(".csv"):
                sys.exit("Not a CSV file")

        # No arguments specified (aside from the current running program)
        case [_]:
            sys.exit("Too few command-line arguments")

        # Catch-all wildcard for an argument list with too many arguments
        case _:
            sys.exit("Too many command-line arguments")

    return path


# Returns a file stream from a provided path,
# or exits the program if the file could not be opened
def get_file_from_path(path: str) -> io.TextIOWrapper:
    try:
        return open(path, "r", newline="")
    except OSError:
        sys.exit("File does not exist")


# Returns the data from a CSV file structured as a tuple,
# where the first item contains a list of headers,
# and the second item contains the actual data (a 2D list of values)
def get_data_from_csv_file(file: io.TextIOWrapper):
    # Creates an iterator over the data read from the file
    reader = csv.reader(file, delimiter=",")

    # Separates the first row of data (used as headers for the table)
    headers = next(reader)

    # Stores the rest of the rows into a list
    data = []
    for row in reader:
        data.append(row)

    return headers, data


# Loads a CSV file from a user-provided command-line argument
# and displays a table containing data from the file
def main():
    path = get_path_from_args()
    file = get_file_from_path(path)
    headers, data = get_data_from_csv_file(file)

    print(tabulate.tabulate(data, headers, "grid"))

    file.close()


if __name__ == "__main__":
    main()
