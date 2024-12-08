"""
Description:

  53. Maximum Subarray

  Given an integer array nums, find the subarray with the largest sum, and return its sum.

  Example 1:
  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: The subarray [4,-1,2,1] has the largest sum 6.

  Example 2:
  Input: nums = [1]
  Output: 1
  Explanation: The subarray [1] has the largest sum 1.

  Example 3:
  Input: nums = [5,4,-1,7,8]
  Output: 23
  Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-08

Version:
    1.1.0

Algorithm Implementation:
    Kadane's Algorithm:
        0) init variables max_sum and curr_sum to nums[0] and curr_sum, respectively.
        1) During the iteration, update the curr_sum with the curr_value
        2) Check if the curr_sum is greater than max_sum, if it is update the max_sum
        3) if the curr_sum becomes negative, make it zero.
        4) return max_sum

Complexities:

    Obvious Approach:
        Time: O(n^2), where  is the length of nums list (nested for loops)
        Space: O(1), we only store two additional variables

    Subtle Approach:
        Time: O(n), where n is the length of nums list
        Space: O(1), we only store two additional variables


Tryouts:

  max_sum = -1
  curr_sum = 0

              p
  n = [-3,-2,-1]

                  p
  n = [-2, 7, -3, 4]


  curr_sum = 8
  max_sum  = 8
"""

from typing import List


class Solution:
    def max_subarray_obvious(self, nums: List[int]) -> int:

        max_sum = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
            curr_sum = 0

        return max_sum

    def max_subarray_kadane(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return None

        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


def test_max_subarray():
    solution = Solution()

    # Test Obvious Solution
    nums = [-3, -2, -1]
    assert solution.max_subarray_obvious(nums) == -1

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.max_subarray_obvious(nums) == 6

    nums = [5, 4, -1, 7, 8]
    assert solution.max_subarray_obvious(nums) == 23

    # Test Kadane's Algorithm Implementation
    nums = [-3, -2, -1]
    assert solution.max_subarray_kadane(nums) == -1

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.max_subarray_kadane(nums) == 6

    nums = [5, 4, -1, 7, 8]
    assert solution.max_subarray_kadane(nums) == 23

    nums = []
    assert solution.max_subarray_kadane(nums) == None

    print("All tests passed!")


test_max_subarray()
