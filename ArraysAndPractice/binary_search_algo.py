"""
Author: Felix
-------
Date: 15 - February - 2022
----
Last Modified: 23 - July - 2022
--------------

Binary Search algorithm on a sorted list
"""


def binarySearch(arr, target):
    """
    Binary Search Algorithm
    """
    lower = 0
    high = len(arr) - 1

    while lower <= high:
        mid_index = (lower + high) // 2
        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] > target:
            high = mid_index - 1
        else:
            lower = mid_index + 1
    return -1


if __name__ == "__main__":
    lst = [1, 2, 7, 14, 18, 20]
    target_val = [2, 0, 14, 18, 20, 100]
    for val in target_val:
        search_result = binarySearch(lst, val)
        if search_result == -1:
            print("Item not found")
        else:
            print(f"The element {val} is at index {search_result}")
