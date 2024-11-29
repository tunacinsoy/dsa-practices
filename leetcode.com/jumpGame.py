"""

Description:
  55. Jump Game

  You are given an integer array nums.
  You are initially positioned at the array's first index,
  and each element in the array represents your maximum jump length at that position.

  Return true if you can reach the last index, or false otherwise.

  Example 1:

    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


  Example 2:

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what.
    Its maximum jump length is 0, which makes it impossible to reach the last index.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-29

Version:
    1.0.0

Algorithm Implementation:

       i
      [2,3,0,1,4]

       i
      [3,2,1,0,4]

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

Complexities:
  Subtle Approach:
    Time: O(n) where n is the length of nums list
    Space: O(1), we only use one additional variable to store max_jump
"""

from typing import List


class Solution:
    def is_end_reachable(self, nums: List[int]) -> bool:

        # This value represents:
        # From the starting position of nums list, which index is the farthest that I can jump to?
        max_jump = 0
        for i in range(len(nums)):
            # If I cannot jump to the current index from the beginning of the list, return false
            if i > max_jump:
                return False

            # Can I jump even farther from the current index compared to previous max_jump?
            max_jump = max(max_jump, nums[i] + i)

            # If we can jump to the last element of the nums list, then we are good
            if max_jump >= len(nums) - 1:
                return True


def test_is_end_reachable():
    solution = Solution()

    nums = [2, 3, 1, 1, 4]
    assert solution.is_end_reachable(nums) == True

    nums = [3, 2, 1, 0, 4]
    assert solution.is_end_reachable(nums) == False


test_is_end_reachable()
print("All tests passed!")
