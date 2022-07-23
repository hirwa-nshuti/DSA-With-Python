"""
Author: Felix
-------
Date: 15 - February - 2022
----
Last Modified: 23 - July - 2022
--------------

Implementing the linear search on an array in three different conditions.
1. Searching for element in sorted array
2. Searching for element in unsorted array
3. Searching for the smallest value in a unsorted array

"""


class Linearsearch:
    """
    The Linear search class
    """
    def __init__(self, searching: list):
        """
        Initializing our linear search
        :param searching: A list containing elements of array
        """
        self.searching = searching
        self.n_elements = len(self.searching)

    def search_sorted(self, element):
        """
        Searching in sorted array
        :param element: Element to be searched
        :return: Index where element is located or None when not found
        """
        for i in range(self.n_elements):
            if self.searching[i] == element:
                return i
            elif self.searching[i] > element:
                return None
        return None

    def search_unsorted(self, data):
        """
        Searching for element in unsorted array
        :param data: element to be searched
        :return: Index where data is located or None if not found
        """

        for i in range(self.n_elements):
            if self.searching[i] == data:
                return i
        return None

    def search_smallest_val(self):
        """
        Searching for the smallest value in an array
        :return: Index and the smallest value
        """
        small = self.searching[0]
        index = 0
        for i in range(self.n_elements):
            if small > self.searching[i]:
                small = self.searching[i]
                index = i
        return small, index


if __name__ == "__main__":
    data_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Searching in a sorted array")
    sorted_search = LinearSearch(data_sorted)
    for _ in range(2):
        search_ele = int(input("Enter the value to search: \n"))
        index_sorted = sorted_search.search_sorted(search_ele)
        if index_sorted is not None:
            print(f"The element {search_ele} is found at {index_sorted}")
        else:
            print("Element not found")

    print("\nSearching in an Unsorted array\n")
    unsorted_arr = [12, 43, 21, 90, 1, 0, 19, 2]
    unsorted_search = LinearSearch(unsorted_arr)
    for _ in range(2):
        search_ele = int(input("Enter the value to search: \n"))
        index_unsort = unsorted_search.search_unsorted(search_ele)
        if index_unsort is not None:
            print(f"The element {search_ele} is found at {index_unsort}")
        else:
            print("Element not found")

    print("\nSearching smallest value in an unsorted array\n")
    un_arr = [12, 281, 21872, -12, 18271, 12, 10, 9, 26, 54, 28]
    search_small = LinearSearch(un_arr)
    smallest, index_s = search_small.search_smallest_val()
    print(f"The smallest number in array is {smallest} and is located at {index_s}")
