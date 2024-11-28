"""

Description:
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    1) Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
    2) The remaining elements of nums are not important as well as the size of nums.
    3) Return k.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-28

Version:
    1.0.0

Algorithm Implementation:

  # CASE 1
  [1,1,2,3,4,5,6] -> [1,2,3,4,5,6], k = 6

               D
             S -> return S
  [1,2,3,4,5,6,1]

             k
               i
  [1,2,3,4,5,6,6]


Complexities:
  Time: O(n) where n is the length of nums list
  Space: O(1), we only initialize a single variable k extra, and we do modification in-place
"""

from typing import List


class Solution:
    def remove_duplicates_in_sorted_list(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)

        k = 0
        # i will end its loop before k, so we are secure in terms of indexOutOfBounds
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1


def validate_remove_duplicates_in_sorted_list():
    solution = Solution()

    # --- Test Cases ---

    # Test Case #1
    nums = [1, 1, 2, 3, 4, 5, 6]
    assert solution.remove_duplicates_in_sorted_list(nums) == 6
    assert nums[:6] == [1, 2, 3, 4, 5, 6]

    # Test Case #2
    nums = []
    assert solution.remove_duplicates_in_sorted_list(nums) == 0
    assert nums == []

    # Test Case #3
    nums = [1, 1, 2, 3, 4, 5, 5, 6]
    assert solution.remove_duplicates_in_sorted_list(nums) == 6
    assert nums[:6] == [1, 2, 3, 4, 5, 6]

    # Test Case #4
    nums = [1, 1, 1, 2, 3, 4, 5, 5, 6, 6, 6]
    assert solution.remove_duplicates_in_sorted_list(nums) == 6
    assert nums[:6] == [1, 2, 3, 4, 5, 6]


validate_remove_duplicates_in_sorted_list()
print("All tests passed!")
