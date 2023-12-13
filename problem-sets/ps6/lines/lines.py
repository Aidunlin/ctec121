# PS-6 Lines of Code
# Aidan Linerud

import io
import sys


# Returns a python file path from command-line arguments,
# or exits the program if there's too many/few arguments
# (or if the file is not a Python file)
def get_path_from_args() -> str:
    match sys.argv:
        # Only allowed case
        # The wildcard "_" skips the first argument (which is always the current running program)
        case [_, path]:
            if not path.endswith(".py"):
                sys.exit("Not a Python file")

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
        return open(path, "r")
    except OSError:
        sys.exit("File does not exist")


# Checks if a string is blank (just whitespace) or is a comment (#)
def is_line_blank_or_comment(line: str) -> bool:
    return line.lstrip() == "" or line.lstrip().startswith("#")


# Returns the number of lines (that aren't blank or comments) in the provided file
def count_lines_in_file(file: io.TextIOWrapper) -> int:
    line_count = 0

    for line in file:
        # Increments line_count if the line has code
        if not is_line_blank_or_comment(line):
            line_count += 1

    return line_count


# Loads a Python file from a user-provided command-line argument
# and displays the number of lines of code in that file
def main():
    path = get_path_from_args()
    file = get_file_from_path(path)
    print(count_lines_in_file(file))

    # Closes the file to prevent memory leaks
    file.close()


if __name__ == "__main__":
    main()
