"""
Author: Felix
-------
Date: 23 - February - 2022
----
Last Modified: 24 - February - 2022
--------------

Sorting an unsorted sequence using different Algorithms:

1. Bubble Sorting
2. Selection sorting
3. Insertion Sorting

"""


from typing import List


class Sorting:
    def __init__(self, seq: List) -> None:
        self.seq = seq
        self.length = len(seq)

    def Display(self) -> None:
        print(self.seq)

    def bubble_sort(self) -> None:
        is_sorted = False
        for i in range(self.length - 1):
            for j in range(i, self.length - 1):
                if self.seq[j] > self.seq[j + 1]:
                    self.seq[j], self.seq[j + 1] = self.seq[j + 1], self.seq[j]
                    is_sorted = True
            if is_sorted == False:
                break

    def selection_sort(self) -> None:
        for i in range(self.length - 1):
            small_ndx = i
            for j in range(i + 1, self.length):
                if self.seq[j] < self.seq[small_ndx]:
                    small_ndx = j
            if small_ndx != i:
                self.seq[i], self.seq[small_ndx] = self.seq[small_ndx], self.seq[i]

    def insertion_sort(self) -> None:
        for i in range(1, self.length):
            data = self.seq[i]
            position = i
            while position > 0 and data < self.seq[position - 1]:
                self.seq[position] = self.seq[position - 1]
                position -= 1
            self.seq[position] = data


if __name__ == "__main__":
    to_sort1 = Sorting([10, 2, 18, 4, 31, 13, 15, 23, 51, 29, 64])
    print("Before Bubble Sort")
    to_sort1.Display()
    print("After Bubble Sort")
    to_sort1.bubble_sort()
    to_sort1.Display()

    to_sort2 = Sorting([10, 2, 5, 18, 4, 31, 13, 15, 23, 51, 29, 64])
    print("\nBefore Selection sort")
    to_sort2.Display()
    print("After Selection Sort")
    to_sort2.selection_sort()
    to_sort2.Display()
    to_sort3 = Sorting([10, 2, 5, 18, 4, 31, 13, 15, 23, 51, 29, 64])
    print("\nBefore Insertion sort")
    to_sort3.Display()
    print("After Insertion Sort")
    to_sort3.selection_sort()
    to_sort3.Display()
