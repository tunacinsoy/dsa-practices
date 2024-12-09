"""

Description:
  12. Integer to Roman

 Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

  Symbol       Value
  I             1
  V             5
  X             10
  L             50
  C             100
  D             500
  M             1000
  For example, 2 is written as II in Roman numeral, just two ones added together.
  12 is written as XII, which is simply X + II.
  The number 27 is written as XXVII, which is XX + V + II.

  Roman numerals are usually written largest to smallest from left to right.
  However, the numeral for four is not IIII. Instead, the number four is written as IV.
  Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
  There are six instances where subtraction is used:

  I can be placed before V (5) and X (10) to make 4 and 9.
  X can be placed before L (50) and C (100) to make 40 and 90.
  C can be placed before D (500) and M (1000) to make 400 and 900.
  Given a roman numeral, convert it to an integer.


  Example 1:
  Input: s = "III"
  Output: 3
  Explanation: III = 3.

  Example 2:
  Input: s = "LVIII"
  Output: 58
  Explanation: L = 50, V= 5, III = 3.

 Example 3:
  Input: s = "MCMXCIV"
  Output: 1994
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-09

Version:
    1.0.0

Algorithm Implementation:
  Key Point: While iterating s, check the char that comes after curr char, and if its value is less than curr_char, then subtract from the sum, otherwise add it to the sum.

Complexities:
  Time: O(n) where n is the length of input string
  Space; O(1)
Tryouts:

"""


class Solution:
    def roman_to_int(self, s: str) -> int:

        roman_table = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        result = 0
        i = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_table.get(s[i]) < roman_table.get(s[i + 1]):
                result -= roman_table.get(s[i])
            else:
                result += roman_table.get(s[i])

        return result


def test_roman_to_int():
    solution = Solution()

    s = "MMMDCCXLIX"
    assert solution.roman_to_int(s) == 3749

    s = "LVIII"
    assert solution.roman_to_int(s) == 58

    s = "MCMXCIV"
    assert solution.roman_to_int(s) == 1994

    print("All tests passed!")

    pass


test_roman_to_int()
