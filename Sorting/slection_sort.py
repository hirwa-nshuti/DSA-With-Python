def selection_sort(lst):
    size = len(lst)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]


if __name__ == "__main__":
    arr = [3, 2, 0, 9, 12, 32, 23, 10]
    selection_sort(arr)
    print(arr)
