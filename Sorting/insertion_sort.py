def insertion_sort(lst:list): 
    for i in range(1, len(lst)):
        anchor = lst[i]
        j = i - 1
        while j >= 0 and anchor < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
            lst[j+1] = anchor


if __name__ == "__main__":
    arr = [3, 2, 0, 9, 12, 32, 23, 10]
    insertion_sort(arr)
    print(arr)
    