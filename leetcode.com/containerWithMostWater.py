"""
Description:

  11. Container with Most Water
  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

  Find two lines that together with the x-axis form a container, such that the container contains the most water.

  Return the maximum amount of water a container can store.

  Notice that you may not slant the container.

  Example 1:

  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49

  https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

  Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
  In this case, the max area of water (blue section) the container can contain is 49.

  Example 2:

  Input: height = [1,1]
  Output: 1

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  1) Init two pointers, left and right
  2) init while loop, while left is less than right
  3) at each step calculate area, and do  max_area = max(current_area, max_area)
  4) Increment left, if it is less than right OR decrement right, if it is less than left
  5) ret max_area

Complexities:
    Time: O(n) where n is the length of the list.
    Space: O(1) only three integers are stored additionally.

"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left <= right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def test_max_area():

    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49

    height = [1, 1]
    assert solution.maxArea(height) == 1


test_max_area()
print("all tests passed!")
