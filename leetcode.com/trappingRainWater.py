"""
Disclaimer:
  One of the hardest questions I have ever solved in my entire life,
  please do not get suicidal while you are trying to understand it.
  Enjoy life.

Description:

  42. Trapping Rain Water

  Given n non-negative integers representing an elevation map where the width of each bar is 1,
  compute how much water it can trap after raining.

  Example 1:

  https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  Explanation: Elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
  In this case, 6 units of rain water (blue section) are being trapped.


Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-01

Version:
    1.0.0

Algorithm Implementation:

The current index can store water according to formula:

  min(max_left,max_right) - height[i]

  Why `min(max_height_of_its_left, max_height_of_its_right)` ?
    Because even though the max_of_right is greater than max_of_left, the bottleneck
    becomes the left, since the water would drop off. That's why, always the min of max_of_left and max_of_right
    would be considered.

  Why `- height[i]` ?

    Because if the current index contains zero block, it means that water can fill in there, however
    if it has a height, water cannot go inside of the block, apparently. That's why we need to subtract the height[i].

  How to iterate?

    We only care about the min(max_height_of_its_left, max_height_of_its_right). So, we need to iterate the one that is
    smaller. if left is smaller, then it should be incremented; if right is smaller, then it should be decremented.


   _ _
    -

Complexities:
    Time: O(n) where n is the length of the list.
    Space: O(1) only three integers are stored additionally.



                                           R
                           L
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

    max_left = 2
    max_right = 1
    sum = 1



    Key Point: Water can't be trapped in edges of height list, so we are actually considering
    heights that are between them.

    Key Point: I do not know from which index I should start iterating over height list, that's why,
    there are two pointers that both iterate over height list, according to if clauses.

                      r
                  l
    height = [1,2,2,1,3] => 1

              l     r
    height = [3,2,2,1,1] => 0

    max_left = 3
    max_right = 1

    sum = 0

"""

from typing import List


class Solution:

    def compute_trapping_water(self, height: List[int]) -> int:
        # An empty list is passed
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        sum = 0

        while left < right:
            if max_left <= max_right:
                # Incrementing left pointer. Right now, left points to the index
                # that we will evaluate its water volume.
                left += 1
                # What if, current height is greater than max_left? Then, this index becomes
                # its own bottleneck.
                max_left = max(max_left, height[left])
                sum += max_left - height[left]
            else:
                # Decrementing right pointer. Right now, right points to the index
                # that we will evaluate its water volume.
                right -= 1
                # What if, current height is greater than max_right? Then, this index becomes
                # its own bottleneck.
                max_right = max(max_right, height[right])
                sum += max_right - height[right]
        return sum


def test_compute_trapping_water():

    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    assert solution.compute_trapping_water(height) == 6


test_compute_trapping_water()
print("All tests passed!")
