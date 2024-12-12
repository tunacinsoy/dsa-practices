"""
2558. Take Gifts From the Richest Pile

Description:
  You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

  Choose the pile with the maximum number of gifts.
  If there is more than one pile with the maximum number of gifts, choose any.
  Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
  Return the number of gifts remaining after k seconds.

Example 1:
  Input: gifts = [25,64,9,4,100], k = 4
  Output: 29
  Explanation:
  The gifts are taken in the following way:
  - In the first second, the last pile is chosen and 10 gifts are left behind.
  - Then the second pile is chosen and 8 gifts are left behind.
  - After that the first pile is chosen and 5 gifts are left behind.
  - Finally, the last pile is chosen again and 3 gifts are left behind.
  The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

Example 2:

  Input: gifts = [1,1,1,1], k = 4
  Output: 4
  Explanation:
  In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
  That is, you can't take any pile with you.
  So, the total gifts remaining are 4.

Algorithm Implementation:


Complexities:
  Obvious Approach:
    Time: O(kn) where n is the length of the list, and k is how many seconds
    Space: O(1) we only use two additional variables

  Subtle Approach:
    Time: O(logn) we use max_heap, and we only need to pop the root of the heap every time
    Space: O(n) we use heap structure

"""

from typing import List
import math
import heapq


class Solution:
    def take_gifts_obvious(self, gifts: List[int], k: int) -> int:

        if not gifts:
            return

        def replace_gifts():
            max_index = 0
            max_pile = 0

            for i in range(len(gifts)):
                if gifts[i] > max_pile:
                    max_pile = gifts[i]
                    max_index = i

            # Here, I know which value to change
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        for i in range(0, k):
            replace_gifts()

        return sum(gifts)

    def take_gifts_max_heap(self, gifts: List[int], k: int) -> int:
        max_heap = []
        # [1,2,3,4,5] - > [-1,-2,-3,-4,-5]
        for gift in gifts:
            max_heap.append(-gift)
        heapq.heapify(max_heap)

        for _ in range(k):
            max_gift = -(heapq.heappop(max_heap))

            remaining_gift = math.floor(math.sqrt(max_gift))

            heapq.heappush(max_heap, -remaining_gift)

        return -sum(max_heap)

        pass


gifts = [25, 64, 9, 4, 100]
solution = Solution()
print(solution.take_gifts_obvious())

gifts = [1, 1, 1, 1]
solution = Solution()
print(solution.take_gifts_obvious())
