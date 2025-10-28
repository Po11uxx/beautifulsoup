from bs4 import BeautifulSoup, SoupStrainer
import sys

def extract_all_tags(path):
    tags = SoupStrainer(True)

    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml", parse_only=tags)

    for tag in soup.find_all(True):
        print(tag.name)

if __name__ == "__main__":
    path = sys.argv[1]
    extract_all_tags(path)