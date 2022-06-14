"""
Finding all missing values in an unsorted array.
"""

def find_missing(array):
    low = min(array)
    high = max(array)
    helper = [False] * (high)
    for i in array:
        helper[i - 1] = True
    for j in range(low, high):
        if helper[j] == False:
            print(j + 1)


if __name__ == "__main__":
    arr = [1, 100]
    find_missing(arr)
