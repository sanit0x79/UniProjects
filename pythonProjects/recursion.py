#!/usr/bin/env python3

def one_to_sum(n):
    """
    Sum all integer values from 1 to n
    """
    if n == 0:
        return 0
    else:
        return n + one_to_sum(n - 1)

def starts_with(s, L):
    if L == "":
        return []
    elif s == L[0][:len(s)]:
        return [L[0]] + starts_with(s, L[1:])
    else:
        return starts_with(s, L[1:])
