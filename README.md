# dictmerge

Merge dicts without mutating them.

```pycon
>>> d1 = {'a': 1}
>>> d2 = {'b': 2}
>>> dictmerge(d1, d2, moar=3)
{'a': 1, 'b': 2, 'moar': 3}
```

As of Python 3.5 you can use the following syntax for this purpose:

```pycon
>>> d1 = {'a': 1}
>>> d2 = {'b': 2}
>>> {**d1, **d2}
{'b': 2, 'a': 1}
>>> {**d1, **d2, **{'moar': 3}}
{'b': 2, 'moar': 3, 'a': 1}
```

# Installation

```console
$ pip install dictmerge
```
