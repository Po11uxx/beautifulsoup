from .. import BeautifulSoup
from ..filter import SoupReplacer

def test_simple_replacement():
    html = "<html><body><b>Bold text</b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    assert soup.find("b") is None

def test_multiple_replacements():
    html = "<b>one</b><b>two</b>"
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    all_strongs = soup.find_all("strong")
    assert len(all_strongs) == 2
