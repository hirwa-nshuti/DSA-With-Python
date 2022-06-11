""""
A Menu driven program for list operations
"""
def sumation(lst:list):
    return sum(lst)


def indexing(lst:list, index):
    x = lst[index]
    return x

def appending(lst:list, element):
    lst.append(element)

def inserting(lst:list, index, element):
    if index in range(len(lst)):
        lst.insert(index, element)
    else:
        return "Index error"
def copy_list(lst:list):
    copied = lst.copy()
    return copied

def extending(lst:list, extenstion):
    lst.extend(extenstion)

def removing(lst:list, value):
    lst.remove(value)

def sorting(lst:list):
    lst.sort()

def reversing(lst:list):
    lst = lst[::-1]


def clearing(lst:list):
    lst.clear()
def get_inputs():
    inputs = []
    x = int(input("Enter the number of values to store in a list: "))
    for _ in range(x):
        inputs.append(int(input("Enter the element and press enter: ")))
    return inputs
if __name__ == "__main__":
    keep_running = True
    data = get_inputs()
    while keep_running:
        print("\nList operations select from")
        print("Press 1 : To find sum of list elements")
        print("Press 2 : To find index of given element")
        print("Press 3 : To append element to a list")
        print("Press 4 : To insert into a  list")
        print("Press 5 : To copy list elements")
        print("Press 6 : To extend the list")
        print("Press 7 : To remove element from the list")
        print("Press 8 : To sort the list elements")
        print("Press 9 : To reverse the list")
        print("Press 10 : To clear the list")
        print("Press 0 : To quit the program\n")

        print(f"\nThe list we have now is {data}\n")
        key = int(input("Select the operation key: "))

        if key == 0:
            prompt_user = input("Do you want to quit y/n: ")
            if prompt_user == "y":
                keep_running = False
                break
            elif prompt_user == "n":
                continue
        elif key == 1:
            print(f"\nSum of your list is {sumation(data)}")
        elif key == 2:
            idx = int(input("Enter the index to look up to: "))
            print(f"\nElement found at index {idx} is {indexing(data, idx)}")
        elif key == 3:
            el = int(input("Enter the element to append: "))
            appending(data, el)
            print(f"\nThe appended list is: {data}")
        elif key == 4:
            idx = int(input("Enter the index to insert to: "))
            el = int(input("Enter the element to insert: "))
            inserting(data, idx, el)
        elif key == 5:
            copied = copy_list(data)
            print(f"\nCopied list is: {copied}")

        elif key == 6:
            print("\nEnter elements to extend to a list")
            to_ext = get_inputs()
            extended = extending(data, to_ext)
            print(f"\nExtended list is: {extended}")
        elif key == 7:
            rem = int(input("Enter the value to remove: "))
            removing(data, rem)
            print(f"\nAfter removing {rem}, the list is {data}")

        elif key == 8:
            sorting(data)
            print(f"\nAfter soring the list is {data}")
        elif key == 9:
            reversing(data)
            print(f"The reversed list is {data}")
        elif key == 10:
            clearing(data)
            print(f"After clearing all elements the list is {data}")
