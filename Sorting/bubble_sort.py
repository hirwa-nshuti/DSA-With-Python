def bubble_sort(lst):
    size = len(lst)
    is_sorted = False

    for i in range(size-1):
        for j in range(size-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_sorted = True
        if not is_sorted:
            break


if __name__ == "__main__":
    arr=[3, 2, 0, 9, 12, 32, 23, 10]
    bubble_sort(arr)
    print(arr)    
