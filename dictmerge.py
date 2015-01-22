import collections


def dictmerge(*dicts, **kwargs):
    """
    Merges an arbitrary number of dicts and kwargs into a single (new) dict.
    Inputs are unaffected.

    Usage:

        >>> d1 = {'a': 1}
        >>> d2 = {'b': 2}
        >>> m = dictmerge(d1, d2, moar=3)
        >>> sorted(m.items())
        [('a', 1), ('b', 2), ('moar', 3)]

    """
    result = {}
    for d in dicts:
        if isinstance(d, collections.Mapping):
            result.update(d)
        elif isinstance(d, collections.Iterable):
            for e in d:
                result.update(e)
    result.update(kwargs)
    return result
