"""
Author: Felix
------
Date: 15 - February - 2022
----
Last Modified: 23 - July - 2022
-------------
"""
from binary_search_algo import binary_search


def test_binary_search():
    """
    Testing the binary search algorithm
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    lst = [1, 2, 7, 14, 18, 20]
    target_val = [2, 0, 14, 18, 20, 100]

    results = []

    for i in target_val:
        results.append(binary_search(lst, i))

    assert results == [0, -1, 3, 4, 5, -1]


if __name__ == "__main__":
    test_binary_search()
