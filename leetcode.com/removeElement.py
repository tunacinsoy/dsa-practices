"""

Description:

    Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in nums in-place.
    The order of the elements may be changed.
    Then return the number of elements in nums which are not equal to `val`.

    Consider the number of elements in nums which are not equal to val be k,
    to get accepted, you need to do the following things:

    1) Change the array `nums` such that the first `k` elements of `nums contain the elements which are not equal to `val`.
    2) The remaining elements of `nums` are not important as well as the size of `nums. Return `k`.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-28

Version:
    1.0.0

Algorithm Implementation:

  # The trick is, we do not need to delete the all occurrances of val,
  # we just need to make sure that they do not appear in [:k] part.

  Input: nums = [3,2,2,3], val = 3
  Output: 2, nums = [2,2,_,_]

         i
      k

  [2,2,2,3]

Complexities:
  Time: O(n) where n is the length of nums list
  Space: O(1), we only use a single integer for k

"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:

    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k


# Example usage:
nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]
