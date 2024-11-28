"""

Description:
    80. Remove Duplicates from Sorted Array II

    Given an integer array nums sorted in non-decreasing order,
    remove some duplicates in-place such that each unique element appears at most twice.
    The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages,
    you must instead have the result to be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates,
    then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array.
    You must do this by modifying the input array in-place with O(1) extra memory.

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

  [1,1,2,2,3,3,3,4,5,6] -> [1,1,2,2,3,3,4,5,6, _,_,_], k = 9

       k
      i
  [1,1,2,2,3,3,4,5,6,6]


  # Case 2

         k
         i
  [1,1,2,2]


Complexities:
  Time: O(n), where n is the length of nums list
  Space: O(1), we only use one more variable as k, and we change values in-place
"""

from typing import List


class Solution:
    def remove_duplicates_in_sorted_array_second(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):

            # Here, we check numbers which repeated three times or more, such as: [1,1,1]
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k


def validate_remove_duplicates_in_sorted_array_second():

    solution = Solution()

    # Test Case 1
    nums = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6]
    assert solution.remove_duplicates_in_sorted_array_second(nums) == 9
    assert nums[:9] == [1, 1, 2, 2, 3, 3, 4, 5, 6]

    # Test Case 2
    nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    assert solution.remove_duplicates_in_sorted_array_second(nums) == 5
    assert nums[:5] == [1, 2, 2, 3, 3]


validate_remove_duplicates_in_sorted_array_second()
print("All tests passed!")
