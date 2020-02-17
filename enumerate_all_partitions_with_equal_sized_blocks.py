import itertools
import functools
import math

def enumerate_all_partitions_with_equal_sized_blocks(s, k):
    """Returns a frozenset of all all possible partitions of a set s which have all blocks of equal size. 
    Let n = len(s). Returns 0 if k does not divide n.

    There are math.factorial(n) / (math.factorial(n/k) * ((math.factorial(k)) ** (n/k))) such partitions.

    Closest reference or definition of this problem I can find is the following StackOverflow post:
        https://cs.stackexchange.com/questions/79562/enumerate-partitions-of-a-set-with-blocks-of-equal-size

    It points to a related section in this paper https://www.doi.org/10.1137/S0097539791202647

    >>> enumerate_all_partitions_with_equal_sized_blocks({1,2,3,4}, 2) == frozenset([\
        frozenset([frozenset([1, 3]), frozenset([2, 4])]),\
        frozenset([frozenset([1, 2]), frozenset([3, 4])]),\
        frozenset([frozenset([2, 3]), frozenset([1, 4])])\
    ])
    True

    >>> enumerate_all_partitions_with_equal_sized_blocks({1,2,3,4,5,6}, 3) == frozenset([\
        frozenset([frozenset([2, 3, 5]), frozenset([1, 4, 6])]),\
        frozenset([frozenset([1, 3, 4]), frozenset([2, 5, 6])]),\
        frozenset([frozenset([3, 4, 6]), frozenset([1, 2, 5])]),\
        frozenset([frozenset([2, 4, 6]), frozenset([1, 3, 5])]),\
        frozenset([frozenset([1, 4, 5]), frozenset([2, 3, 6])]),\
        frozenset([frozenset([1, 3, 6]), frozenset([2, 4, 5])]),\
        frozenset([frozenset([1, 5, 6]), frozenset([2, 3, 4])]),\
        frozenset([frozenset([1, 2, 3]), frozenset([4, 5, 6])]),\
        frozenset([frozenset([1, 2, 6]), frozenset([3, 4, 5])]),\
        frozenset([frozenset([3, 5, 6]), frozenset([1, 2, 4])])\
    ])
    True

    >>> s, k = {1,2,3,4,5,6,7,8,9,10,11,12}, 4
    >>> n = len(s)
    >>> expected_number_of_partitions = math.factorial(n) / (math.factorial(n/k) * ((math.factorial(k)) ** (n/k)))
    >>> actual_number_of_partitions = len(enumerate_all_partitions_with_equal_sized_blocks(s, k))
    >>> expected_number_of_partitions == actual_number_of_partitions
    True
    """
    if len(s) == k:
        return frozenset({frozenset({frozenset(s)})})
    
    possible_first_choices = map(set, itertools.combinations(s, k))

    def find_partitions_with_this_first_choice(so_far, possible_first_choice):
        all_possible_partitions_of_remainder = enumerate_all_partitions_with_equal_sized_blocks(
            s - possible_first_choice, k
        )

        partitions_involving_this_choice = set(map(
            lambda possible_partition_of_remainder: frozenset({frozenset(possible_first_choice)})\
                | possible_partition_of_remainder,
            all_possible_partitions_of_remainder
        ))

        return so_far | partitions_involving_this_choice

    return functools.reduce(
        find_partitions_with_this_first_choice, possible_first_choices, frozenset()
    )