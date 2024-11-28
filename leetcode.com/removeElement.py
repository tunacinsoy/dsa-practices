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


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


# Test cases
def test_remove_element():
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    assert k == 2
    assert nums[:k] == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

    nums = [1]
    val = 1
    k = solution.removeElement(nums, val)
    assert k == 0
    assert nums[:k] == []

    nums = [4, 5]
    val = 4
    k = solution.removeElement(nums, val)
    assert k == 1
    assert nums[:k] == [5]

    print("All test cases passed!")


# Run the tests
test_remove_element()
