from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def test_iter_simple():
    html = "<p>hello</p>"
    soup = BeautifulSoup(html, "html.parser")

    names = [type(node).__name__ for node in soup]
    assert "BeautifulSoup" in names
    assert "Tag" in names
    assert "NavigableString" in names

def test_iter_nested():
    html = "<div><p><b>text</b></p></div>"
    soup = BeautifulSoup(html, "html.parser")

    from bs4.element import Tag, NavigableString

    nodes = [
        node.name if isinstance(node, Tag) else str(node)
        for node in soup
    ]

    # DFS 顺序验证
    assert nodes == [
        '[document]',     # soup root
        'div',
        'p',
        'b',
        'text'
    ]

from bs4 import Comment

def test_iter_mixed_nodes():
    html = "<div>hi<!--c--></div>"
    soup = BeautifulSoup(html, "html.parser")

    found_comment = any(isinstance(n, Comment) for n in soup)
    found_string = any(str(n) == "hi" for n in soup)

    assert found_comment
    assert found_string

def test_iter_empty():
    soup = BeautifulSoup("", "html.parser")
    nodes = list(soup)
    assert len(nodes) == 1   # only root
    assert nodes[0] is soup

def test_iter_with_replacer():
    html = "<b>hi</b>"
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    tag_names = [n.name for n in soup if hasattr(n, "name")]
    assert "strong" in tag_names
