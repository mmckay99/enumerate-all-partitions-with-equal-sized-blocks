This repository holds a Python function `enumerate_all_partitions_with_equal_sized_blocks` and some small doctests.

Given a set `s` and integer `k`, the function returns a set (`frozenset`) of all possible partitions of `s` into blocks of size `k`. If `k` does not divide `len(s)` then the function returns an empty set.

I used this function to generate possible perfect `k`-dimensional matchings of a complete `k`-uniform hypergraph.

Closest reference or definition of this problem I can find is the following StackOverflow post:
    https://cs.stackexchange.com/questions/79562/enumerate-partitions-of-a-set-with-blocks-of-equal-size

It points to a related section in this paper https://www.doi.org/10.1137/S0097539791202647
