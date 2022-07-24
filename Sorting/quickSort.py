"""
Quick Sort we can take first element of array and put in
middle where left is less than reference
and the right is greater than reference
This is a divide and conquer problem
The method of dividing is called partition
Partition schemes: Hoare Partition, Lomuto Partition
"""


def swap(a, b, arr):
    if a != b:
        arr[a] = arr[a] + arr[b]
        arr[b] = arr[a] - arr[b]
        arr[a] = arr[a] - arr[b]


def partition(elements, start, end):
    p_index = start
    ref = elements[p_index]
    while start < end:
        while start < len(elements) and elements[start] <= ref:
            start += 1

        while elements[end] > ref:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(p_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        par_index = partition(elements, start, end)
        quick_sort(elements, start, par_index - 1)
        quick_sort(elements, par_index + 1, end)


if __name__ == "__main__":
    el = [
        [11, 9, 29, 7, 2, 15, 28],
        [],
        [10, 8, 2, 1, 0],
        [1, 2],
        [20, 1920, 0, 0]]
    for element in el:
        quick_sort(element, 0, len(element) - 1)
        print(f"The sorted array: {element}")
