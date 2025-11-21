# Milestone-4

### Objective
In Milestone-4, we extend the existing `BeautifulSoup` class so that **the soup object itself becomes iterable**.  
This allows users to perform:

```bash
    soup = BeautifulSoup(html_doc, "html.parser")
    
    for node in soup:
        print(node)
```
### How to Achieve
added `__iter__()` and `_traverse()` in class `BeautifulSoup`
```bash
    def __iter__(self):
        """
        Iterate over all nodes in the parse tree.
        DFS traversal. Does not materialize the nodes into a list.
        """
        yield from self._traverse(self)

    def _traverse(self, node):
        """
        Depth-first traversal generator.
        Yields the node itself, then recursively yields its children.
        """
        yield node

        # Only Tag objects have .contents
        if hasattr(node, "contents"):
            for child in node.contents:
                yield from self._traverse(child)
```

### Test
Created a new test file which contains 5 test modules:
`beautifulsoup/bs4/tests/test_iter_soup.py`

##### Test root iteration
```bash
    def test_iter_root():
        ...
```

##### Test nested DFS
```bash
    def test_iter_nested():
        ...
```

##### Test sibling traversal
```bash
    def test_iter_siblings():
        ...
```

##### Test navigable strings included
```bash
    def test_iter_strings():
        ...
```

##### Test empty soup
```bash
    def test_iter_empty():
        ...
```

run the test:
```bash
  pytest bs4/tests/test_iter_soup.py -q
```