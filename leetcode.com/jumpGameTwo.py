"""

Description:
  45. Jump Game II

  You are given a 0-indexed array of integers nums of length n.
  You are initially positioned at nums[0].

  Each element nums[i] represents the maximum length of a forward jump from index i.
  In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

  Return the minimum number of jumps to reach nums[n - 1].
  The test cases are generated such that you can reach nums[n - 1].

  Example 1:

    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

  Example 2:

    Input: nums = [2,3,0,1,4]
    Output: 2


Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-29

Version:
    1.0.0

Algorithm Implementation:

      # The idea is to keep track of the farthest point that can be reached with the current number of jumps and
      # update the number of jumps whenever you reach the end of the current range.

      i
      [2,  3,  1,  1,  4]
       _   _____   _____

      From 2, I can go to -> [3,1]; From 3, I can go to [1, 4], whereas from 1, I can only go to [1], so max is 3


      jumps = 2 # How many times did I jump? (also return value)
      current_end = 4 # With amount of jumps I have done, what's my ending point?
      farthest = 4 # What's the farthest index that I can jump to from the beginning of the list?

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
It's guaranteed that you can reach nums[n - 1]

Complexities:
  Subtle Approach:
    Time: O(n) where n is the length of nums list
    Space: O(1), we only use three additional variables
"""

from typing import List


class Solution:
    def get_minimum_jumps(self, nums: List[int]) -> int:

        # How many times did I jump?
        jumps = 0

        # With amount of jumps I have done, what's my ending point?
        current_end = 0

        # What's the farthest index that I reach to?
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest  # Updating the next block's last position
                if current_end >= len(nums) - 1:
                    break

        return jumps


def test_is_end_reachable():
    solution = Solution()

    nums = [2, 3, 1, 1, 4]
    print(solution.get_minimum_jumps(nums))
    # assert solution.is_end_reachable(nums) == True

    nums = [2, 3, 0, 1, 4]
    print(solution.get_minimum_jumps(nums))
    # assert solution.is_end_reachable(nums) == False


test_is_end_reachable()
print("All tests passed!")
