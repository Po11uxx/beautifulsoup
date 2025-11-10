from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


# Tag name replacement
def test_tag_name_replacement():
    html = "<html><body><p>Normal text</p><b>Important text</b></body></html>"
    replacer = SoupReplacer(name_xformer=lambda t: "blockquote" if t.name == "b" else t.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.blockquote is not None


# Attribute replacement
def test_attribute_replacement():
    html = "<html><body><p class='note'>Normal text</p><div id='keep'>Block</div></body></html>"
    replacer = SoupReplacer(attrs_xformer=lambda t: {"id": "new"} if "class" in t.attrs else t.attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "id" in soup.p.attrs


# Attribute deletion
def test_delete_attribute():
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    html = "<html><body><p class='remove-me'>A</p><span>B</span></body></html>"
    replacer = SoupReplacer(xformer=remove_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "class" not in soup.p.attrs


# Combined transformations
def test_combined_transformations():
    def rename(tag): return "div" if tag.name == "span" else tag.name
    def replace_attrs(tag): return {"style": "bold"}

    html = "<html><body><span>Hello</span><span>World</span></body></html>"
    replacer = SoupReplacer(name_xformer=rename, attrs_xformer=replace_attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.div["style"] == "bold"


# No replacer provided
def test_no_replacer():
    html = "<html><body><b>bold</b><p>plain</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    assert soup.b is not None


# Legacy interface compatibility
def test_simple_replacer():
    replacer = SoupReplacer("b", "blockquote")
    html = "<html><body><b>bold</b><p>plain</p></body></html>"
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.blockquote is not None