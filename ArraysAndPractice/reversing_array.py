def reverse_arr(lst):
    size = len(lst) - 1
    i = 0
    while(i < size):
      	
        lst[i], lst[size] = lst[size], lst[i]
        i += 1
        size -= 1

if __name__ == "__main__":
    data = [1, 2]
    reverse_arr(data)
    print(data)