"""
Author: Felix
------
Date: 15 - February - 2022
----
Last Modified: 23 - July - 2022
-------------
"""


def find_missing(array):
    """
    Finding the missing element in an unsorted array
    Parameters
    ----------
    array
        An array to look up in
    Returns
    -------
    ret
        a list with missing values
    """
    low = min(array)
    high = max(array)
    helper = [False] * (high)
    for i in array:
        helper[i - 1] = True
    for j in range(low, high):
        if helper[j] is False:
            print(j + 1)


if __name__ == "__main__":
    arr = [1, 100]
    find_missing(arr)
