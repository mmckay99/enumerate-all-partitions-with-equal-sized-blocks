import itertools
import functools

def enumerate_all_partitions_with_equal_sized_blocks(s, k):
    """Returns a frozenset of all all possible partitions of a set s which have all blocks of equal size. 
    Returns 0 if k does not divide len(s).

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


print(enumerate_all_partitions_with_equal_sized_blocks(set(range(15)), 3))

