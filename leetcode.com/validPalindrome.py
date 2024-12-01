"""

Description:
  125. Valid Palindrome

  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
  and removing all non-alphanumeric characters,
  it reads the same forward and backward. Alphanumeric characters include letters and numbers.

  Given a string s, return true if it is a palindrome, or false otherwise.

  Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

  Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

  Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-01

Version:
    1.0.0

Algorithm Implementation:

    rl
   amma

     l
     r
   amkma

  TO:DO
  1) Convert input string into lowercase
  2) replace all non-alphanumeric characters with ""
  3) init two pointers, one from beginning one from end
  4) Init while loop, check each char one by one


Complexities:
  Time:  O(n) where n is the length of string
  Space: O(1), because we only store two additional variable (pointers)

"""


class Solution:
    def is_palindrome(self, phrase: str) -> bool:

        # 1) Convert input string into lowercase
        phrase = phrase.lower()

        # 2) replace all non-alphanumeric characters with ""
        clean_text = ""
        for char in phrase:
            if char.isalnum():
                clean_text += char

        # 3) init two pointers, one from beginning one from end
        left_pointer = 0
        right_pointer = len(clean_text) - 1

        # Edge case for empty string
        if len(clean_text) == 0:
            return True

        # 4) Init while loop, check each char one by one
        while left_pointer < len(clean_text) and right_pointer >= 0:

            if left_pointer >= right_pointer:
                break

            if clean_text[left_pointer] != clean_text[right_pointer]:
                return False

            left_pointer += 1
            right_pointer -= 1

        return True


def test_is_palindrome():

    solution = Solution()

    # Test Case 1
    assert solution.is_palindrome("A man, a plan, a canal: Panama") == True

    # Test Case 2
    assert solution.is_palindrome("race a car") == False

    # Test Case 3
    assert solution.is_palindrome(" ") == True


test_is_palindrome()
print("All tests passed!")
