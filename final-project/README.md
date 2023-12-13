# md2html

[View video demo](https://youtu.be/YJ7-uKHKiZU)

## Brief Description

md2html is a command-line app that converts a Markdown file to an HTML file. The user specifies the file they want to convert as a command-line argument, and optionally the path/name of the outputted HTML file.

The `os` module is used to validate and extract the file extension of the input/output files. The `re` module is used in the bulk of the conversion logic to pattern match Markdown syntax (and directly replace inline syntax, such as **bold text** and `code`). `sys` is used to get command line arguments and exit the system early.

The `md2html.md` and `md2html.html` example files are used to test that the program outputs correct HTML for each implemented part of the Markdown syntax. This is unrelated to `test_project.py`, which performs unit tests against several functions in the project.

## `Document`

I created a rudimentary object oriented approach to build and manage basic HTML block elements when converting Markdown. This is to support elements within elements, and keep track of creating things such as lists and blockquotes. The `Document` class, like the actual [DOM element](https://developer.mozilla.org/en-US/docs/Web/API/Document), acts as a sort of entry point for the HTML. Because Markdown syntax is much simpler than HTML, I don't have to implement the majority of the DOM API, just basic elements that contain references to their respective parent and children elements.

Where `Document` differs from the DOM API the most is creating new elements. Instead of creating a variable to store the result of `document.createElement()` and then using `appendChild` on some other element, the `Element` class has a simple `add_child()` method that does both of those things.

## `Element`

`Element`s only store their tag name, list of children, and their parent element. Because I did not have to implement text nodes, the list of children in any particular `Element` can include elements as well as strings. Outside of just representing HTML DOM, the `add_text()` method converts any inline Markdown expressions to HTML.

## Conversion Logic

The first half of the process is to read through each line of Markdown in the input file. To keep track of how each line can possible affect the output of the next line (e.g. lists), I use two additional variables to store whether the last line was empty, and the current element that's being added to or modified.

In the `convert_line()` function, the code goes through a large if/elif/else block to test various regular expressions. These, in order, pertain to horizontal lines, headings (h1-h6), blockquotes, unordered lists, and ordered lists. If none of these match for the current line, it will simply create a paragraph (or a line break in the current paragraph) that contains the text, or do nothing (but set `last_line_empty` to `True`) if the line is blank.

The branches for horizontal lines and headings will always set `current_element` to the document's body, meaning those elements will always be put directly in the body. Meanwhile, the blockquote and list branches will first check if the current element is already the same as what the branch pertains to, and only creating a brand new blockquote/list otherwise.

## `InlineConverter`

Generally speaking, the `InlineConverter` class and `INLINE_CONVERTERS` list aren't exactly required for the program to work. However, running [`Pattern.sub()`](https://docs.python.org/3/library/re.html#re.Pattern.sub) for every inline Markdown expression means managing a long list of fairly unreadable regex patterns and associated replacers. Therefore, the purpose of `InlineConverter` (and the list) is to simply organize them and make them as readable as possible. The good news is, `re`'s replacement strings are extremely simple to understand; they use a `\\#` where each capture group should be put during the replacement.

[RegExr](https://regexr.com/) was a vital tool when ensuring each regex pattern used actually works. I also made sure that each inline expression could be correctly identified *within* each other by doing two things:

- Each converter only converts **one** type of Markdown expression
- Run converters in a specific order

By running the **bold** converter before *italics*, text that is both ***bolded and italicized*** will always be surrounded with `<em><strong>...</strong></em>`. Running the titled image and titled link converters first will ensure the correct number of capture groups for those converters.

## Stringify

The second half of the process is to output each element in the document in the form of strings. Because I wanted to include indents in the outputted HTML, I did not override the built-in `__str__` methods, and included a `depth` parameter to indicate how many times the element should be indented.

Starting with the document, I return `<!DOCTYPE html>` before calling `to_string()` on the top-level HTML element. By default, `depth` is zero, so there will be no indentation for that element. It then checks itself if it's an element with a self-closing tag (i.e. horizontal rule or line break), in which case it would simply return the tag itself. Because it isn't it then checks if it only contains a single string. If so, it will print itself and the string together in a single line for brevity. Because, again, it doesn't (as it includes head and body elements), it will loop over its children, calling each child element's `to_string()` method with `depth + 1`, or if the particular child is a string, simply concatenate it with a newline and proper indentation.
