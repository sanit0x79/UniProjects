#!/usr/bin/env python3

def three_ize(L):
    """ three_ize is a function that accepts a list and
        returns a list of elements each three times as large
    """

    lc = [3 * x for x in L]
    return lc


def scale(L, scale_factor):

    lc = [scale_factor * x for x in L]
    return lc

print(scale([70, 80, 420], 0.1))




def three_ize_by_index(L):
    """three_ize_by_index has the same behaviour as three_ize
    but it uses the INDEX of each element, instead of using
    the elements themselves -- this is much more flexible!
    """

    n = len(L)
    lc = [3 * L[i] for i in range(n)]
    return lc
