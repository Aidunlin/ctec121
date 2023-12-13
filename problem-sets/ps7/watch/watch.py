# watch.py
# Aidan Linerud

import re


# Extracts and returns a shortened YT video link from an HTML iframe embed
def parse(html: str) -> str:
    # Try to match the HTML iframe embed, with a capture group for the YT video's ID
    id_match = re.match("^<iframe.*src=\"[^\"]*youtube.com\/embed\/([^\"]*)\".*><\/iframe>$", html)

    # Return the shortened video link if the match and capture group were successful
    if id_match:
        return "https://youtu.be/" + id_match.group(1)


def main():
    # Extracts and displays a shortened YT video link from an HTML iframe embed
    print(parse(input("HTML: ")))


if __name__ == "__main__":
    main()
