"""
**QUESTION:** Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible. Write a function to help Bob locate the card.

Typical approach to the problem
-------------------------------
**Problem statement:** We have a task to search for an element in a decreasing ordered list and return its index.

**Inputs:** The sorted sequence ex: [10, 5, 3, 2 , 1], and the variable to search ex: 3.
**Outputs:** The position of searched variable ex: 2 if not present the function will return 0
"""

test_cases = [
    {
        'inputs': {
            'cards': [10, 8, 5, 4, 2, 1],
            'query': 5, },
        'output': 2
    },
    {
        'inputs': {
            'cards': [8, 6, 2, 1],
            'query': 8, },
        'output': 0
    },
    {
        'inputs': {
            'cards': [],
            'query': 5, },
        'output': -1
    },
    {
        'inputs': {
            'cards': [10, 9, 5, 3, 2, 1],
            'query': 1, },
        'output': 5
    },
    {
        'inputs': {
            'cards': [10],
            'query': 7, },
        'output': -1
    },
]


# First approach linear search
def find_card_linear(cards, query):
    size = len(cards)
    if size == 0:
        return -1
    for i in range(size):
        if cards[i] == query:
            return i
    return -1


def find_card(cards, query):
    pass


# Test cases
if __name__ == "__main__":
    for test in test_cases:
        print(f"Inputs: {test['inputs']}")
        print(f"Output: {test['output']}")
        print("----------")
        result = find_card_linear(**test['inputs']) == test['output']
        if result:
            print("Test passed\n")
        else:
            print("Test failed\n")
