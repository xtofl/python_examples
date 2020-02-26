#!/usr/bin/env python3

__doc__ = """
It came to my attention that some people prefer working
with lists over tuples, because... you can sort a list,
you can append to a list, ...

I think lists, as any mutable data structures, are more
hard to use than you would think.

Compare the two variations of the same algorithm to produce
a triangle of numbers.  The test with lists fails, while
the test with tuples succeeds.

Can you spot the error?
"""
import pytest

def tree_of_lists(n):
    result = []
    line = []
    for i in range(n):
        result.append(line)
        line.append(i)
    return result

def tree_of_tuples(n):
    result = tuple()
    line = tuple()
    for i in range(n):
        result = result + (line,)
        line = line + (i,)
    return result

@pytest.mark.xfail
def test_lists():
    assert tree_of_lists(3) == [[], [0], [0, 1]]

def test_tuples():
    assert tree_of_tuples(3) == (tuple(), (0,), (0, 1))

