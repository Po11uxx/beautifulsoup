from bs4 import BeautifulSoup, SoupStrainer
import sys

def extract_hyperlinks(path):
    a_tag = SoupStrainer("a")

    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml", parse_only=a_tag)

    for a in soup.find_all("a"):
        print(a)

if __name__ == "__main__":
    path = sys.argv[1]
    extract_hyperlinks(path)