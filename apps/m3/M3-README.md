# Milestone-3
In Milestone-3, the previous constructor `SoupReplacer(og-tag, alt-tag)` is reused and added optional keyword arguments that presents a different interface to the users, and is capable of doing more powerful node transformations: 
`SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`

Transformer (`xformer`) arguments are supposed to be functions that take a tag in the tree as argument. `name_xformer` and `attrs_xformer` return replacements for the tag’s name and attributes, respectively; `xformer` is a more powerful function that can have side effects on the tag and doesn’t return anything.
### Test
```bash
  pytest bs4/tests/test_replacerM3.py -q
```

### Task-7 with SoupReplacer
```bash
  python ./apps/m3/task7.py ./apps/m3/small1.html
```

