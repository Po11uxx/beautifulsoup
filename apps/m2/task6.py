from bs4 import BeautifulSoup, SoupReplacer
import sys

def replace_tags_during_parse(path, og_tag, alt_tag):
    print("og:", og_tag)
    print("alt:", alt_tag)
    replacer = SoupReplacer(og_tag, alt_tag)
    print(type(replacer))
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
        print(soup.prettify())

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python task6.py <html_file> <og_tag> <alt_tag>")
    else:
        replace_tags_during_parse(sys.argv[1], sys.argv[2], sys.argv[3])
