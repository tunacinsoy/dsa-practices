"""

Description:
  189. Rotate Array

  Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

  Example 1:

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]


Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-29

Version:
    1.0.0

Algorithm Implementation:

  nums = [1,2,3] k = 1
  nums = [3,1,2] -> [2,3,1] -> [1,2,3] -> [3,1,2]

                [3]   +    [1,2] => [3,1,2]
  nums[:] = nums[-k:] + nums[:-k]


  nums = [1,2,3,4,5,6,7], k = 3
  nums = [7,1,2,3,4,5,6] -> [6,7,1,2,3,4,5] -> [5,6,7,1,2,3,4]

             [5,6,7] +  [1,2,3,4] => [5,6,7,1,2,3,4]
  nums[:] = nums[-k:] + nums[:-k]


Complexities:
  Naive Approach:
    Time: O(n) where n is the length of nums list
    Space: O(n) where n is the length of nums list

  Subtle Approach:
    Time: O(n) where n is the length of nums list
    Space: O(n) because of concatenation (sublists take space)
"""

from typing import List


class Solution:
    def rotate_array_naive(self, nums: List[int], k: int) -> None:

        if len(nums) == 0:
            return

        # If k is greater than the length of nums list, then some operations
        # would be redundant, since if we change the nums list len(nums) time,
        # we would end up in initial state of nums list.
        k = k % len(nums)

        # Last elements that will go to the beginning of the list
        last_elements = nums[len(nums) - k : len(nums)]

        # First elements that will go to the end of the list
        first_elements = nums[: len(nums) - k]

        for num in first_elements:
            last_elements.append(num)

        nums[:] = last_elements

    def rotate_array_subtle(self, nums: List[int], k: int) -> None:

        if len(nums) == 0:
            return

        k %= len(nums)
        # print(k)
        nums[:] = nums[-k:] + nums[:-k]


def test_rotate_array_naive():
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    solution.rotate_array_naive(nums, k)
    # print(f"Inside test func: {nums}")
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = []
    k = 5
    solution.rotate_array_naive(nums, k)
    assert nums == []

    nums = [-1, -100, 3, 99]
    k = 2
    solution.rotate_array_naive(nums, k)
    assert nums == [3, 99, -1, -100]


def test_rotate_array_subtle():

    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    solution.rotate_array_subtle(nums, k)
    # print(f"Inside test func: {nums}")
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = []
    k = 5
    solution.rotate_array_subtle(nums, k)
    assert nums == []

    nums = [-1, -100, 3, 99]
    k = 2
    solution.rotate_array_subtle(nums, k)
    assert nums == [3, 99, -1, -100]
    pass


test_rotate_array_naive()
test_rotate_array_subtle()
print("All tests passed!")
