import os
import re
import sys


class InlineConverter:
    def __init__(self, name: str, pattern: str, replacer: str):
        self._name = name
        self._pattern = re.compile(pattern)
        self._replacer = replacer

    def convert(self, text: str) -> str:
        return self._pattern.sub(self._replacer, text)


INLINE_CONVERTERS = [
    InlineConverter(
        name="code",
        pattern=r"`\s*([^\*]+)\s*`",
        replacer=r"<code>\1</code>",
    ),
    InlineConverter(
        name="bold",
        pattern=r"\*\*\s*([^\*]+)\s*\*\*",
        replacer=r"<strong>\1</strong>",
    ),
    InlineConverter(
        name="italics",
        pattern=r"\*\s*([^\*]+)\s*\*",
        replacer=r"<em>\1</em>",
    ),
    InlineConverter(
        name="titled_image",
        pattern=r'!\[(.*)\]\(([^"\s]*)\s+"([^"]*)"\s*\)',
        replacer=r'<img src="\2" alt="\1" title="\3">',
    ),
    InlineConverter(
        name="image",
        pattern=r'!\[(.*)\]\(([^"\s]*)\s*\)',
        replacer=r'<img src="\2" alt="\1">',
    ),
    InlineConverter(
        name="titled_link",
        pattern=r'\[(.*)\]\(([^"\s]*)\s+"([^"]*)"\s*\)',
        replacer=r'<a href="\2" title="\3">\1</a>',
    ),
    InlineConverter(
        name="link",
        pattern=r'\[(.*)\]\(([^"\s]*)\s*\)',
        replacer=r'<a href="\2">\1</a>',
    ),
]


class Element:
    def __init__(self, tag: str):
        self.tag = tag
        self.children: list[Element | str] = []
        self.parent: Element | None = None

    def to_string(self, depth=0):
        indent = "  " * depth

        if self.tag in ["hr", "br"]:
            return f"{indent}<{self.tag}>"

        if len(self.children) == 1 and isinstance(self.children[0], str):
            html = self.children[0]
        else:
            html = ""

            for child in self.children:
                html += "\n"

                if isinstance(child, Element):
                    html += child.to_string(depth + 1)
                else:
                    html += "  " * (depth + 1) + child

            html += f"\n{indent}"

        return f"{indent}<{self.tag}>{html}</{self.tag}>"

    def add_child(self, tag: str):
        child = Element(tag)
        child.parent = self
        self.children.append(child)
        return child

    def add_text(self, text: str):
        text = text.strip()
        for CONVERTER in INLINE_CONVERTERS:
            text = CONVERTER.convert(text)
        self.children.append(text)


class Document:
    def __init__(self, title: str):
        self.html = Element("html")
        self.html.add_child("head").add_child("title").add_text(title)
        self.body = self.html.add_child("body")

    def to_string(self):
        return f"<!DOCTYPE html>\n{self.html.to_string()}\n"


def get_path_ext(path: str) -> str:
    return os.path.splitext(path)[1].lower().removeprefix(".")


def get_io_paths(args: list[str]) -> tuple[str, str]:
    match args:
        case [_, input_path, output_path]:
            if get_path_ext(input_path) != "md":
                raise ValueError(f"md2html: {input_path} is not an MD file")

            if get_path_ext(output_path) != "html":
                raise ValueError(f"md2html: {output_path} is not an HTML file")

        case [_, input_path]:
            if get_path_ext(input_path) != "md":
                raise ValueError(f"md2html: {input_path} is not an MD file")

            output_path = os.path.splitext(input_path)[0] + ".html"

        case _:
            print("Usage: python project.py INPUT [OUTPUT]")
            print("Converts an INPUT markdown file to an OUTPUT html file.")
            print("By default, the OUTPUT path is the same as the INPUT path,")
            print("but ending with '.html' instead.")
            raise ValueError(f"md2html: no input path specified")

    return input_path, output_path


def convert_line(
    line: str,
    document: Document,
    last_line_empty: bool,
    current_element: Element,
) -> tuple[bool, Element]:
    if re.match(r"^[\*\-_]{3}.*", line):
        current_element = document.body
        current_element.add_child("hr")
        last_line_empty = False
    elif heading_match := re.match(r"^(#{1,6})\s*(.*)", line):
        current_element = document.body
        tag = f"h{len(heading_match.group(1))}"
        current_element.add_child(tag).add_text(heading_match.group(2))
        last_line_empty = False
    elif blockquote_match := re.match(r"^\>\s*(.*)", line):
        if current_element.tag != "blockquote":
            current_element = document.body.add_child("blockquote")

        current_element.add_child("p").add_text(blockquote_match.group(1))
        last_line_empty = False
    elif ul_item_match := re.match(r"^[-\*+]\s*(.*)", line):
        if current_element.tag != "ul":
            current_element = document.body.add_child("ul")

        current_element.add_child("li").add_text(ul_item_match.group(1))
        last_line_empty = False
    elif ol_item_match := re.match(r"^\d+\.\s*(.*)", line):
        if current_element.tag != "ol":
            current_element = document.body.add_child("ol")

        current_element.add_child("li").add_text(ol_item_match.group(1))
        last_line_empty = False
    elif len(line):
        if last_line_empty:
            current_element = document.body.add_child("p")
            current_element.add_text(line)
        elif current_element.tag == "p":
            current_element.add_child("br")
            current_element.add_text(line)

        last_line_empty = False
    else:
        last_line_empty = True

    return last_line_empty, current_element


def main():
    try:
        input_path, output_path = get_io_paths(sys.argv)
    except ValueError as excinfo:
        sys.exit(excinfo.args[0])

    try:
        input_file = open(input_path)
    except IOError:
        sys.exit(f"md2html: could not open {input_path}")

    document = Document(os.path.basename(input_path))
    current_element = document.body
    last_line_empty = True

    for line in input_file:
        last_line_empty, current_element = convert_line(
            line.strip(), document, last_line_empty, current_element
        )

    input_file.close()

    try:
        output_file = open(output_path, "w")
    except IOError:
        sys.exit(f"md2html: could not write to {output_path}")

    output_file.write(document.to_string())
    output_file.close()
    print(f"md2html: {input_path} successfully converted to {output_path}")


if __name__ == "__main__":
    main()
