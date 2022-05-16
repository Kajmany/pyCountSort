#!usr/bin/env python 3
# CS162
# Phoenix Angulo
# Completed 5/XX/22
"""Implements count sort in Python. The journey is the point."""
# Time Complexity: O(n+k)
# Space Complexity: O(n+k)?
# Very cool, very fast, but only if we're sorting integers with a relatively small range.
# Step 1: Count the number of occurances of each number
# Step 2: Process the count array
# Step 3: Use the count array to write out sorted array


def count_sort(in_ints: list, value_range: range) -> list:
    # 1: Count Occurances
    count_list = [0 for i in value_range]  # We'll need to tally each possible int
    for i in in_ints:
        count_list[i] += 1  # Each number already has its own cell to tally to!
    # 2: Add count of i to next cell
    for i in range(len(in_ints) - 1):
        count_list[i + 1] += count_list[i]


if __name__ == "__main__":
    in_ints = [0, 2, 2, 6, 4, 2, 9, 6, 1, 4]
    value_range = range(0, 10)  # Remember upper bound is exclusive!
    count_sort(in_ints, value_range)
