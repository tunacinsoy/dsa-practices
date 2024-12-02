"""
Description:

  150. Evaluate Reverse Polish Notation

  You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
  Evaluate the expression. Return an integer that represents the value of the expression.


  Note that:

  The valid operators are '+', '-', '*', and '/'.
  Each operand may be an integer or another expression.
  The division between two integers always truncates toward zero.
  There will not be any division by zero.
  The input represents a valid arithmetic expression in a reverse polish notation.
  The answer and all the intermediate calculations can be represented in a 32-bit integer.

  Example 1:
  Input: tokens = ["4","13","5","/","+"]
  Output: 6
  Explanation: (4 + (13 / 5)) = 6

  Example 2:
  Input: tokens = ["2","1","+","3","*"]
  Output: 9
  Explanation: ((2 + 1) * 3) = 9

  Example 3:
  Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  Output: 22
  Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
  = ((10 * (6 / (12 * -11))) + 17) + 5
  = ((10 * (6 / -132)) + 17) + 5
  = ((10 * 0) + 17) + 5
  = (0 + 17) + 5
  = 17 + 5
  = 22

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  1) Init list as stack
  2) start iterating over tokens list, and check if current str is a digit, if it is, push (append) to stack
  3) if it is a math operator, pop the last two elements from the list, do the math operation, and push it onto stack again
  4) at last, return the element that is stored in stack (there should be a one stack)

Complexities:

    Time :  O(n), where n is the length of nums list
    Space:  O(n), we use stack to store numbers

Tryouts:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

Stack:

  22
"""

from typing import List


class Solution:

    def calculate(self, num1: int, num2: int, operation: str) -> int:

        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return int(num1 / num2)
        else:
            return 0

    def evaluate_reverse_polish_notation(self, tokens: List[str]) -> int:
        numbers_stack = []

        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operations:
                latter_number = int(numbers_stack.pop())
                prior_number = int(numbers_stack.pop())
                result = self.calculate(prior_number, latter_number, token)
                numbers_stack.append(str(result))
            else:
                numbers_stack.append(token)

        return int(numbers_stack[0])


def test_evaluate_reverse_polish_notation():

    solution = Solution()

    tokens = ["1", "2", "+"]
    assert solution.evaluate_reverse_polish_notation(tokens) == 3

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert solution.evaluate_reverse_polish_notation(tokens) == 22


test_evaluate_reverse_polish_notation()
print("All tests passed!")
