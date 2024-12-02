"""
Description:

  11. Container with Most Water
  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

  You must write an algorithm that runs in O(n) time.

  Example 1:

  Input: nums = [100,4,200,1,3,2]
  Output: 4
  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

  Example 2:

  Input: nums = [0,3,7,2,5,8,4,6,0,1]
  Output: 9

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  We can't use sorting and check the consecutive elements, since it would give O(nlogn) time complexity.

  What we can do is:
    1) store the elements in set(),
    2) then check if the n-1 exits in the set, if it does not, then we find a starting point
    3) then, we can start a loop using n + 1 exists in set, and if it does, increaselength, and
    4) then check max(max_length, curr_length).
    5) return max_length.


Complexities:

    Time: O(n), where n is the length of nums list, (while loop only iterates for candidates who are starting point)
    Space: O(n) where n is the length of nums list



Tryouts:
      p
    [100,4,200,1,3,2]


    (100,4,200,1,3,2)

    curr_length = 0
    max_length = 3

    (1,2,3,4,5)

    p
    [1,2,3,4,5]

    curr_length = 1
    max_length = 0


"""

from typing import List


class Solution:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_length = 0

        for num in nums:

            if (num - 1) not in nums_set:
                curr_length = 1

                # We find a starting point, we need to iterate
                while (num + 1) in nums_set:
                    curr_length += 1
                    num += 1

                max_length = max(max_length, curr_length)
            curr_length = 0

        return max_length


def test_longest_consecutive_sequence():
    solution = Solution()

    # Case 1
    nums = [1, 2, 3, 4, 5]
    assert solution.longest_consecutive_sequence(nums) == 5

    # Case 2
    nums = [1, 1, 1, 1, 1]
    assert solution.longest_consecutive_sequence(nums) == 1

    # Case 3
    nums = [1, 2, 3, 6, 7, 8]
    assert solution.longest_consecutive_sequence(nums) == 3

    # Case 3
    nums = [1, 2, 3, 6, 7]
    assert solution.longest_consecutive_sequence(nums) == 3


test_longest_consecutive_sequence()
print("All tests passed!")
