"""Library of functions for iterating over multi-level iterables."""

from collections.abc import Iterable

def depthflatten(iterable, depth):
    """Iterate over a given number of iterables.
    
    Args:
        iterable: An object which allows iteration, containing at least depth-1
            levels of other iterables.
        depth: An integer specifying the number of layers to flatten over.

    Generates:
        The elements of the iterables at the given depth, consecutively.
    """

    if not isinstance(iterable, Iterable):
        raise TypeError("iterable must be an iterable object")
    if not isinstance(depth, int):
        raise TypeError("depth must be a positive integer")
    if depth < 1:
        raise ValueError("depth must be a positive")

    for elem in iterable:
        if depth > 1:
            for item in flatten(elem, depth - 1):
                yield item
        else:
            yield elem

def depthenum(iterable, depth):
    """Enumerate over a given depth of iterable.
    
    Args:
        iterable: An object which allows iteration, containing at least depth-1
            levels of other iterables.
        depth: An integer specifying the number of layers to flatten over.

    Generates:
        An index tuple with as many entries of depth, along with the element at
            that index.
    """

    if not isinstance(iterable, Iterable):
        raise TypeError("iterable must be an iterable object")
    if not isinstance(depth, int):
        raise TypeError("depth must be a positive integer")
    if depth < 1:
        raise ValueError("depth must be a positive integer")

    for i, elem in enumerate(iterable):
        if depth > 1:
            for indices, item in multenum(elem, depth - 1):
                yield (i,) + indices, item
        else:
            yield (i,),  (elem,)
