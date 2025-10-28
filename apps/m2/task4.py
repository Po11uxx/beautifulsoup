from bs4 import BeautifulSoup, SoupStrainer
import sys

def extract_all_tags_with_id(path):
    tags_with_id = SoupStrainer(True, id=True)

    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml", parse_only=tags_with_id)

    for tag in soup.find_all(True, id=True):
        print(tag)

if __name__ == "__main__":
    path = sys.argv[1]
    extract_all_tags_with_id(path)