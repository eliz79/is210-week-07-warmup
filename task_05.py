#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Mutability differences between string and tuples."""

to_flip = [(1, 2, 3), 'hello']

def flip_keys(to_flip):
    """A function that reverses the data.

    Args:
        to_flip(mixed): An immutable nested list.

    Return:
        The original list with inner elements reserved.

    Examples:
        >>>LIST = [(1,2,3), 'abc']
        >>>NEW = flip_keys(LIST)
        >>>LIST is NEW
        True
        >>>print LIST
        [(3,2,1), 'cba']
    """

    return to_flip

counter = 0
new_flip = []
for value in to_flip:
    if counter < len(to_flip):
        new_flip.append(value[::-1])
