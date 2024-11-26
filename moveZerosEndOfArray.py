"""

Description:
   Move all zeros to the end of an inputListay while maintaining the order of the other elements.
   Given an inputListay of integers, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Constraints:
    You must do this in-place without making a copy of the inputListay.
    Minimize the total number of operations.
    For example, given the input inputListay [0, 1, 0, 3, 12], after calling your function, the inputListay should be [1, 3, 12, 0, 0].

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-26

Version:
    1.0.0

Algorithm Implementation:

    Two pointers:
      `.` points to zero
      `,` index of for loop

    * [1,3,12,5,0] -> [1,3,12,5,0]

                 ,
                 .
    * [1,3,12,0,0] -> [1,3,12,0,0]

               ,
               .
    * [1,0,0,0,0] -> [1,0,0,0,0]


Complexities:
  Time: O(n)
  Space: O(1)
"""

from typing import List


def moveZerosToEnd(inputList: List[int]) -> List[int]:

    length = len(inputList)

    if length < 2:
        print(f"There is not any necessary operation to perform.")
        return inputList

    zero_pointer = 0

    for value in inputList:

        if value != 0:
            inputList[zero_pointer] = value
            zero_pointer += 1

    while zero_pointer < length:
        inputList[zero_pointer] = 0
        zero_pointer += 1

    return inputList


assert moveZerosToEnd([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

assert moveZerosToEnd([0, 0, 0, 0, 1]) == [1, 0, 0, 0, 0]

assert moveZerosToEnd([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

print("All tests passed!")
