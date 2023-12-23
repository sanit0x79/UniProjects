#!/usr/bin/env python3
def is_periodical(s, E):
    if s == "":
        return True

    for element in E:
        if element == s[:len(element)]:
            if is_periodical(s[len(element):], E):
                return True

    return False
