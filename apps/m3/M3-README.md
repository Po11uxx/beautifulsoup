# Milestone-3
### Target
In Milestone-3, the previous constructor `SoupReplacer(og-tag, alt-tag)` is reused and added optional keyword arguments that presents a different interface to the users, and is capable of doing more powerful node transformations: 
`SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`

Transformer (`xformer`) arguments are supposed to be functions that take a tag in the tree as argument. `name_xformer` and `attrs_xformer` return replacements for the tag’s name and attributes, respectively; `xformer` is a more powerful function that can have side effects on the tag and doesn’t return anything.

### How to Achieve
`beautifulsoup/bs4/filter.py`
```bash
    class SoupReplacer(ElementFilter):
        def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
            self.og_tag = og_tag
            self.alt_tag = alt_tag
            self.name_xformer = name_xformer
            self.attrs_xformer = attrs_xformer
            self.xformer = xformer
    
        def replace(self, name: str) -> str :
            if name == self.og_tag:
                return self.alt_tag
            return name
```

`beautifulsoup/bs4/__init__.py`
```bash
    # replacer
    self.replacer = replacer

    if isinstance(builder, type):
        builder = builder()
    if builder is None:
        builder_class = builder_registry.lookup(features)
        if builder_class is None:
            raise FeatureNotFound(
                "Couldn't find a tree builder with the features you requested: %s"
                % features
            )
        builder = builder_class()
    self.builder = builder
    self.is_xml = builder.is_xml

    self.reset()
    self.hidden = True
    self.parse_only = parse_only
    self.builder.initialize_soup(self)
```
`_htmlparser.py`
```bash
    ...
    # replacer
    if hasattr(self.soup, "replacer") and self.soup.replacer:
        name = self.soup.replacer.replace(name)
    ...
    replacer = getattr(self.soup, "replacer", None)
    if replacer and tag is not None:
        if callable(getattr(replacer, "name_xformer", None)) and replacer.name_xformer:
            tag.name = replacer.name_xformer(tag)
        if callable(getattr(replacer, "attrs_xformer", None)) and replacer.attrs_xformer:
            tag.attrs = replacer.attrs_xformer(tag)
        if callable(getattr(replacer, "xformer", None)) and replacer.xformer:
            replacer.xformer(tag)
        elif getattr(replacer, "og_tag", None) and getattr(replacer, "alt_tag", None):
            if tag.name == replacer.og_tag:
                tag.name = replacer.alt_tag
```


### Test
```bash
  pytest bs4/tests/test_replacerM3.py -q
```

### Task-7 with SoupReplacer
```bash
  python ./apps/m3/task7.py ./apps/m3/small1.html
```

