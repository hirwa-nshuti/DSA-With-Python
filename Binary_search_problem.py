"""
QUESTION: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible.
Write a function to help Bob locate the card.

Typical approach to the problem
-------------------------------
Problem statement: We have a task to search for an element in
a decreasing ordered list and return its index.

Inputs: The sorted sequence ex: [10, 5, 3, 2 , 1],
and the variable to search ex: 3.
Outputs: The position of searched variable ex: 2,
if not present the function will return 0
"""


test_cases = [
    {
        "inputs": {
            "cards": [10, 8, 5, 4, 2, 1],
            "query": 5,
        },
        "output": 2,
    },
    {
        "inputs": {
            "cards": [8, 6, 2, 1],
            "query": 8,
        },
        "output": 0,
    },
    {
        "inputs": {
            "cards": [],
            "query": 5,
        },
        "output": -1,
    },
    {
        "inputs": {
            "cards": [10, 9, 5, 3, 2, 1],
            "query": 3,
        },
        "output": 3,
    },
    {
        "inputs": {
            "cards": [10],
            "query": 7,
        },
        "output": -1,
    },
]


# First approach linear search
def find_card_linear(cards, query):
    """
    The Linear search function to return the position of card being searched.

    Parameters
    ----------
    cards
        A descending ordered list of cards numerical values
    query
        A card to look for in the cards input

    Returns
    -------
    ret
        The index position of the card if present and -1 if not present
    """
    size = len(cards)
    if size == 0:
        return -1
    for i in range(size):
        if cards[i] == query:
            return i
    return -1


def find_card_bin(cards, query):
    """
    The Binary search function to return the position of card being searched.

    Parameters
    ----------
    cards
        A descending ordered list of cards numerical values
    query
        A card to look for in the cards input

    Returns
    -------
    ret
        The index position of the card if present and -1 if not present
    """
    left_index = 0
    right_index = len(cards) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = cards[mid_index]
        if mid_number == query:
            return mid_index
        if mid_number < query:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1


def test_function(fun_name, tests):
    """
    Testing the function outputs

    Parameters
    ----------
    fun_name
        The name of function to test
    tests
        Dictionary containing the test cases

    Returns
    -------
    ret
        None
    """
    for test in tests:
        print(f"Inputs: {test['inputs']}")
        print(f"Output: {test['output']}")
        print("----------")
        result = fun_name(**test["inputs"]) == test["output"]
        if result is True:
            print("Test passed\n")
        else:
            print("Test failed\n")


# Test cases
if __name__ == "__main__":
    print("Testing the linear Search approach\n")
    test_function(find_card_linear, test_cases)

    print("Testing the binary search approach\n")
    test_function(find_card_bin, test_cases)
