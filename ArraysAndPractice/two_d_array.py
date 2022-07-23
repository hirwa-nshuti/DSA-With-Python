"""
Author: Felix
------
Date: 15 - February - 2022
-----
Last Modified: 15 - February - 2022
-------------


Trying to implement 2D array basing on 1D array
This array will have methods:
rowsNumber: Returns the number of rows
columnsNumber: Returns the number of columns
clear_2D: Setting the array elements to a given value
getitem: Returns value stored in An array at given index
setitem: Modify array element at a given index to a given value
"""
from .one_d_array import Array


class Array2D:
    def __init__(self, rows: int, columns: int) -> None:
        """
        Initializing number of rows and columns for our array
        :param rows: Number of rows of array
        :param columns: number of columns of array
        """
        self._rowsNumber = Array(rows)
        for i in range(rows):
            self._rowsNumber[i] = Array(columns)

    def rowsNumber(self) -> int:
        """
        counting number of rows
        :return: Number of rows of the 2D array
        """
        return len(self._rowsNumber)

    def columnsNumber(self) -> int:
        """
        counting columns number
        :return: Number of columns of 2D array
        """
        return len(self._rowsNumber[0])

    def clear_2D(self, data) -> None:
        """
        Setting array element to a given value data
        :return: None
        """
        for row in range(self.rowsNumber()):
            self._rowsNumber[row].clear(data)

    def __getitem__(self, indices: list):
        """
        Returning a value at given index
        :param indices: List containing row and column location of element
        :return: element at an index
        """
        assert len(indices) == 2, "Invalid index"
        row = indices[0]
        col = indices[1]
        assert (
            0 <= row < self.rowsNumber() and 0 <= col < self.columnsNumber()
        ), "Index out of range"
        array1D = self._rowsNumber[row]
        return array1D[col]

    def __setitem__(self, indices: list, value) -> None:
        """

        :param indices: list containing row and column location of element
        :param value: A value to be put at index given
        :return: None
        """
        assert len(indices) == 2, "Invalid index try again"
        row = indices[0]
        col = indices[1]
        assert (
            0 <= row < self.rowsNumber() and 0 <= col < self.columnsNumber()
        ), "Index out of range"
        array1D = self._rowsNumber[row]
        array1D[col] = value


if __name__ == "__main__":
    new_arr = Array2D(3, 2)
    print(new_arr)
    print(f"Number of rows in this array is: {new_arr.rowsNumber()}\n")
    print(f"Number of Columns in this array is: {new_arr.columnsNumber()}\n")
    new_arr.clear_2D(12)
    print(new_arr.__getitem__([0, 1]))
    new_arr.__setitem__([1, 1], 5)
    print("Element at index: [1, 1] is: ")
    print(new_arr.__getitem__([1, 1]))
