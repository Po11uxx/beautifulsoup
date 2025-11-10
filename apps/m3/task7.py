import sys

from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def add_class_attr(tag):
    if tag.name == "p":
        tag.attrs["class"] = "test"

def main():
    input_file = sys.argv[1]
    output_file = "./apps/m3/" + "updated_" + input_file.split("/")[-1]

    with open(input_file, "r", encoding="utf-8") as f:
        replacer = SoupReplacer(xformer=add_class_attr)
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

if __name__ == "__main__":
    main()
