"""
Author: Felix
------
Date: 15 - February - 2022
-----
Last Modified: 15 - February - 2022
-------------

Writing an array ADT to implement array operation in python as we initially has python
list and this code will implement array using ctypes module

This array ADT will be 1D array with size elements
Array ADT will have methods like
length: The length of the array
getitem: returning the value at given index
setitem: Converting the element at given index to wanted value
clear: setting all array's elements to a given value
iterator: Traversing through a given array

"""

import ctypes
import random


class Array:
    def __init__(self, size):
        """
        Initializing an array with size elements
        :param size: number of array elements
        """
        assert size > 0, "Array size must be greater than 0"
        self._size = size
        python_array = ctypes.py_object * size
        self._elements = python_array()
        self.clear(None)

    def __len__(self):
        """
        Finding the length of array
        :return: the length of our array
        """
        return self._size

    def __getitem__(self, index: int):
        """
        Returning array element at given index
        :param index: integer, index to which you want to retrieve the value
        :return: array element at given index
        """
        assert len(self) > index >= 0, "Index out of range"
        return self._elements[index]

    def __setitem__(self, index: int, value):
        """
        Setting element at given index to value
        :param index: index at which we want to modify
        :param value: Value that needs to be set
        :return: No return
        """
        assert len(self) > index >= 0, "Index out of range"
        self._elements[index] = value

    def clear(self, value):
        """
        Setting all elements of array to a given element value
        :param value: value to set to be array elements
        :return: No return value
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Traversing through our array
        :return: array iterator to traverse elements
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, our_array):
        self._referenceArray = our_array
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Iterating through an array
        :return: array elements
        """
        if self._current_index < len(self._referenceArray):
            entry = self._referenceArray[self._current_index]
            self._current_index += 1
            return entry
        else:
            raise StopIteration


if __name__ == "__main__":
    new_array = Array(26)
    # Filling array with random values
    for j in range(len(new_array)):
        new_array[j] = random.randrange(1, 65)

    # Finding length length of array
    print("The size of array is: ", new_array.__len__())

    # Setting the element at 5th index of our array to 12
    print(f"The element at 5th index before is: {new_array[5]}")
    new_array.__setitem__(5, 12)
    print(f"The value at 5th index became {new_array[5]}")

    # Getting item at the index value n = 7
    n = 7
    print(f"The element at {n} is {new_array.__getitem__(7)}")

    # Viewing my iterator
    print(new_array.__iter__())

    # Setting array values to 0
    new_array.clear(0)
    print("After setting all elements to zero our array became")
    for element in new_array:
        print(element)
