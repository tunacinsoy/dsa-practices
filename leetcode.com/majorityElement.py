"""

Description:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

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
    [1,2,2,3,2] -> 2


  # CASE 2


Complexities:
  Time: O(n logn) -> where n is the number of elements in nums list, bottleneck is the sorted() function
  Space: O(n) -> where n is the number of elements in nums list
"""

from typing import List


class Solution:
    def find_majority_element(self, nums: List[int]) -> int:

        if not nums:
            return None

        numsDict = {}

        for i in range(len(nums)):

            if nums[i] in numsDict:
                numsDict[nums[i]] += 1
            else:
                numsDict[nums[i]] = 1

        sorted_numsDict = sorted(numsDict.items(), reverse=True, key=lambda x: x[1])

        return sorted_numsDict[0][0]


def test_find_majority_element():

    solution = Solution()

    nums = [3, 2, 3, 2, 2, 3, 3, 3]
    assert solution.find_majority_element(nums) == 3

    nums = []
    assert solution.find_majority_element(nums) == None

    nums = [1, 1, 1, 1]
    assert solution.find_majority_element(nums) == 1

    nums = [1, 1, 2, 2, 2]
    assert solution.find_majority_element(nums) == 2


test_find_majority_element()
print("All tests passed!")
