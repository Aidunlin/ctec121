import project
import pytest


def test_get_path_ext():
    assert project.get_path_ext("helloworld.txt") == "txt"
    assert project.get_path_ext("file-with-two-periods.woah.html") == "html"
    assert project.get_path_ext(".nofilename") == ""


def test_get_io_paths():
    with pytest.raises(ValueError):
        project.get_io_paths(["project.py"])

    with pytest.raises(ValueError):
        project.get_io_paths(["project.py", "file.html"])

    with pytest.raises(ValueError):
        project.get_io_paths(["project.py", "file.md", "image.png"])

    assert project.get_io_paths(["project.py", "file.md"]) == ("file.md", "file.html")


def test_convert_line():
    line = "Test this **super** *cool* ***line***!"
    document = project.Document("Test")
    last_line_empty = True
    current_element = document.body

    last_line_empty, current_element = project.convert_line(
        line, document, last_line_empty, current_element
    )

    assert not last_line_empty
    assert current_element.tag == "p"
    assert len(current_element.children) == 1
    assert current_element.children[0] == "Test this <strong>super</strong> <em>cool</em> <em><strong>line</strong></em>!"
