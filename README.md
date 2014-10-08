# dictmerge

Merge dicts without mutating them.

```pycon
d1 = {'a': 1}
d2 = {'b': 2}
>>> dictmerge(d1, d2)
{'a': 1, 'b': 2}
>>> dictmerge(d1, d2, extra='moar')
{'a': 1, 'b': 2, extra='moar'}
```

# Installation

    pip install dictmerge

