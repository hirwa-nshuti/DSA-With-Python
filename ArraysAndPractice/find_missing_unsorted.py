def find_missing(array):
    """
    Finding the missing element in an unsorted array
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
