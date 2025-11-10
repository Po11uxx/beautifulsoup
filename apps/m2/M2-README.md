# Milestone-2
## Part 1 - SoupStrainer
`apps/m2/task2.py`
 - ```bash
   cd apps/m2
   python task2.py ./wiki_python.html
   
`apps/m2/task3.py`
 - ```bash
   cd apps/m2
   python task3.py ./wiki_python.html
   
`apps/m2/task4.py`
 - ```bash
   cd apps/m2
   python task4.py ./wiki_python.html

## Part 2 — API Function Locations

- BeautifulSoup.__init__ — `bs4/__init__.py`, line 209 
  Initializes the parser and builds the tree.

- BeautifulSoup.find_all — `bs4/element.py`, line 2013  
  Finds all tags matching given criteria.

- BeautifulSoup.prettify — `bs4/element.py`, line 1915
  Pretty-print this PageElement as a string.

- BeautifulSoup.get — `bs4/element.py`, line 1543 
  Returns the value of the 'key' attribute for the tag, or the value given for 'default' if it doesn't have that attribute.

- BeautifulSoup.find — `bs4/element.py`, line 1987
  Look in the children of this PageElement and find the first PageElement that matches the given criteria.

- BeautifulSoup.find_parent — `bs4/element.py`, line 722
  Find the closest parent of this PageElement that matches the given criteria.

- BeautifulSoup.select — `bs4/element.py`, line 2096
  Perform a CSS selection operation on the current element.

- BeautifulSoup.get_test — `bs4/element.py`, line 275
  Get all child strings of this PageElement, concatenated using the given separator.

- SoupStrainer.__init__ — `bs4/element.py`, line 2155  
  Restricts parsing to specific tags or attributes.

## Part 3 - SoupReplacer
`apps/m2/task6.py`
- ```bash
   python -m apps.m2.task6 ./apps/m2/wiki_python.html ./apps/m2/replaced_wiki_python.html b blockquote
