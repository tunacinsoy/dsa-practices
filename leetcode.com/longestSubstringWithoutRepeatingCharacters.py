"""
Description:

  11. Container with Most Water
  Given a string s, find the length of the longest substring without repeating characters.

  Example 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

  Example 2:
  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.

  Example 3:
  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Notice that the answer must be a substring, "pwke" is a `subsequence` and not a `substring`s.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  Key Point: The set that we will initialize is going to store:
    "the longest substring that does not include repetitive characters between pointer r and pointer l"

  1) Init two pointers -> l from beginning, r from beginning + 1 up until length of string
  2) add the char pointed by l into set
  3) if the char pointed by r is not in set, increment r. Else, remove the char pointed by l from set, and increment l
  4) return (r-l+1)

Complexities:

    Time :  O(n), where n is the length of nums list
    Space:  O(n), where n is the length of nums list

Tryouts:

      r
    l
    abcabcbb -> 3

     r
    l
    abcc -> 3

    {"a", "b"}

    longest_substring = 0

"""


class Solution:
    def longest_substring_length(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        # Pointers used for slicing window
        l = 0
        r = 1

        # Set for storing current substring
        char_set = set()

        # Init set with first char
        char_set.add(s[l])

        longest_substring = 0

        while r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                longest_substring = max(longest_substring, r - l + 1)
                r += 1
            else:
                char_set.remove(s[l])
                l += 1

        return longest_substring


def test_longest_substring_length():

    solution = Solution()

    s = "abc"
    assert solution.longest_substring_length(s) == 3

    s = "abcabcbb"
    assert solution.longest_substring_length(s) == 3

    s = ""
    assert solution.longest_substring_length(s) == 0

    s = "aaaaaaa"
    assert solution.longest_substring_length(s) == 1

    s = "q"
    assert solution.longest_substring_length(s) == 1


test_longest_substring_length()
print("All tests passed!")
