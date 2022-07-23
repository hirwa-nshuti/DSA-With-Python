"""
Author: Felix
-------
Date: 22 - February - 2022
----
Last Modified: 23 - July - 2022
--------------

Finding Duplicates in both unsorted list and sorted list.

"""


class Duplicates:
    """
    Duplicates
    """

    def __init__(self, lst: list):
        """
        Initializing our list
        :param lst: A list containing elements of array
        """
        self.lst = lst
        self.length = len(self.lst)

    def findDuplicates(self) -> None:
        """
        Finding Duplicates in the list
        """
        max_el = max(self.lst) + 1
        helper = [0] * max_el
        for i in range(self.length):
            helper[self.lst[i]] += 1
        for i in range(max_el):
            if helper[i] > 1:
                print(f"Element {i} is present {helper[i]} times")


if __name__ == "__main__":
    data_unsort = [8, 3, 6, 4, 6, 5, 6, 8, 2, 7]
    sorted_arr = [1, 1, 1, 3, 5, 6, 9, 9, 9, 10, 15, 15, 17]
    print("Duplicates in an unsorted array")
    array_data = Duplicates(data_unsort)
    array_data.findDuplicates()
    print("Duplicates in a sorted array")
    arr_d = Duplicates(sorted_arr)
    arr_d.findDuplicates()
