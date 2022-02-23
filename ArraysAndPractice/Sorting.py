"""
Author: Felix
-------
Date: 23 - February - 2022
----
Last Modified: 23 - February - 2022
--------------

Sorting an unsorted sequence using different Algorithms:

1. Bubble Sorting

"""

from typing import List


class Sorting:
    def __init__(self, seq: List) -> None:
        self.seq = seq
        self.length = len(seq)

    def Display(self) -> None:
        print(self.seq)

    def bubble_sort(self):
        is_sorted = False
        for i in range(self.length - 1):
            for j in range(i, self.length - 1):
                if self.seq[j] > self.seq[j + 1]:
                    self.seq[j], self.seq[j + 1] = self.seq[j + 1], self.seq[j]
                    is_sorted = True
            if is_sorted == False:
                break


if __name__ == "__main__":
    arr = [10, 2, 18, 4, 31, 13, 5, 23, 51, 29, 64]
    to_sort = Sorting(arr)
    print("Before Bubble Sort")
    to_sort.Display()
    print("After Bubble Sort")
    to_sort.bubble_sort()
    to_sort.Display()
