"""
Description:
  Remove Adjacent Duplicates in String.
  You are given a string s and an integer k.
  Write a function to remove k adjacent duplicates from s where the "adjacent" characters are equal.

  For instance, if k is 3 and the string is "daaabbbaa",
  since we have "aaa" and "bbb" as adjacent triples,
  the function should transform the string to "daa", removing the "bbb" first and then the remaining "aaa".

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-26

Version:
    1.0.0

Algorithm Implementation:

    "daaabbbaa" -> 'daa'

    # Stack Implementation
    [(d,1),(a,2), , , , ->

Complexities:
    Time: O(n)
    Space: O(n)
"""


def remove_duplicates(input: str, k: int) -> str:

    stack = []  # Initiate an empty list (will be used as stack)

    # stack[-1][0] will hold the char
    # stack[-1][1] will hold the occurrance

    for char in input:

        if stack and stack[-1][0] == char:
            stack[-1][
                1
            ] += 1  # Increment the occurrance of the last element in list (aka stack)
        else:
            stack.append([char, 1])  # push a new char with its occurrance

        if stack[-1][1] == k:
            stack.pop()  # If the occcurrance reaches the value k, then pop it

    # Reconstruct the string from the stack
    retStr = ""
    for char, count in stack:
        retStr += char * count

    return retStr


# define test cases

assert remove_duplicates("daaabbbaa", 3) == "daa"
assert remove_duplicates("pbbcggttciiippooaais", 2) == "ps"

print("All tests passed!")
