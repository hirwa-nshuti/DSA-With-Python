from BinarySearch import binarySearch


def test_binary_search():
    lst = [1, 2, 7, 14, 18, 20]
    target_val = [2, 0, 14, 18, 20, 100]

    results = []

    for i in target_val:
        results.append(binarySearch(lst, i))

    assert results == [1, -1, 3, 4, 5, -1]


if __name__ == "__main__":
    test_binary_search()