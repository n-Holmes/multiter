"""Tests for depth-based iterators."""
import pytest

from multiter import depthflatten, depthenum

def test_correct_depth():
    """Check that depth based iterators stop at the desired depth.
    Given a three-dimensional iterable.
    When depthflatten or depthenum are called on the iterable with specified depth.
    Then only the given number of dimensions should be iterated over.
    """

    three_layer_iterable = [
        ['one', 'two', (3, 4)],
        ['five']
    ]

    assert len(list(depthflatten(three_layer_iterable, 1))) == 2
    assert len(list(depthflatten(three_layer_iterable, 2))) == 4
    assert len(list(depthflatten(three_layer_iterable, 3))) == 12

    assert len(list(depthenum(three_layer_iterable, 1))) == 2
    assert len(list(depthenum(three_layer_iterable, 2))) == 4
    assert len(list(depthenum(three_layer_iterable, 3))) == 12
