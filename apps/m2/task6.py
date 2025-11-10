from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
import sys

def replace_tags_during_parse(path, output_path, og_tag, alt_tag):
    replacer = SoupReplacer(og_tag, alt_tag)
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(soup.prettify())

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python task6.py <html_file> <og_tag> <alt_tag>")
    else:
        replace_tags_during_parse(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
