#!/usr/bin/env python3

def list_distance(list1: list[int], list2: list[int]) -> int:
    """Returns the distance between two lists of integers."""
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

assert list_distance([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 11
