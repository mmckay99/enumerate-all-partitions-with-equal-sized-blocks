This repository holds a Python function `enumerate_all_partitions_with_equal_sized_blocks` and some small doctests.
Given a set `s` and integer `k`, the function returns a set (`frozenset`) of all possible partitions of `s` into subsets of size `k`. If `k` does not divide `len(s)` then the function returns an empty set.

There are ![n! / ((n/k)! * ((math.factorial(k)) ** (n/k)))](number_of_partitions_latex.svg) such partitions.

I used this function to generate possible perfect `k`-dimensional matchings of a complete `k`-uniform hypergraph.

Closest reference or definition of this problem I can find is the following StackOverflow post:
    https://cs.stackexchange.com/questions/79562/enumerate-partitions-of-a-set-with-blocks-of-equal-size

It points to a related section in this paper https://www.doi.org/10.1137/S0097539791202647

The number of possible partitions of equal sized blocks is exponential in `len(s)`, so the time taken will of course be exponential in the size of `s`. This function might take longer to execute than you think! Please share any ideas of performance improvements.

For `k=3` I ran the following tests on my machine with 16 GiB RAM and 8 Intel(R) Core i7-7700 CPU @ 3.6GHz CPUs. 

| n (k=3)       | time taken (s)  |
| ------------- | -----:|
| 3   | 0.05 |
| 6  | 0.04 |
| 9 | 0.04 |
| 12 | 1.38 |
| 15 | 815.90 (13 min!) |
