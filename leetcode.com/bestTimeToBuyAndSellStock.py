"""

Description:
  121. Best time to buy and sell stock

  You are given an array prices where prices[i] is the price of a given stock on the ith day.
  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

  Example:

  prices = [1,2,3,4,5,6] -> profit = 5
  prices = [3,4,2,5,6,7,1] -> profit = 5
  prices = [] -> profit = 0
  prices = [1,1,1,1,1] -> profit = 0

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-29

Version:
    1.0.0

Algorithm Implementation:
  Naive Approach:
              P
    prices = [1,2,3,4,5,6] -> 5

    prices = [6,5,4,3,2,1] -> 0

              P
    prices = [6,8,5,3,2,1] -> 0

    max_price = 8
    min_price = 1

    # profit = [sell - buy] -> if < 0, return 0

  Subtle Approach:
    # The left points to the buy day, r points to sell day
    # if r>l => check the profit is greater than max_profit
    # else: do l=r, since we found a lower point then previous one

                r
              l
    prices = [1,2,3,4,5,6] -> 5


Complexities:
  Naive Approach:
    Time: O(n^2), nested loops
    Space: O(1), we only hold one additional variable

  Subtle Approach:
    Time: O(n) where n is the length of prices list
    Space: O(1), we only hold two additional variables
"""

from typing import List


class Solution:
    def max_profit_naive(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

    def max_profit_subtle(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

    def max_profit_subtle_two_pointers(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_profit


def test_max_profit_naive():

    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    solution.max_profit_naive(prices)
    assert solution.max_profit_naive(prices) == 5

    prices = [1, 2, 3]
    assert solution.max_profit_naive(prices) == 2

    prices = [9, 9, 9]
    assert solution.max_profit_naive(prices) == 0

    prices = [7, 6, 4, 3, 1]
    assert solution.max_profit_naive(prices) == 0


def test_max_profit_subtle():
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    solution.max_profit_naive(prices)
    assert solution.max_profit_subtle(prices) == 5

    prices = [1, 2, 3]
    assert solution.max_profit_subtle(prices) == 2

    prices = [9, 9, 9]
    assert solution.max_profit_subtle(prices) == 0

    prices = [7, 6, 4, 3, 1]
    assert solution.max_profit_subtle(prices) == 0

    prices = [7, 1, 5, 3, 6, 4]
    solution.max_profit_naive(prices)
    assert solution.max_profit_subtle_two_pointers(prices) == 5

    prices = [1, 2, 3]
    assert solution.max_profit_subtle_two_pointers(prices) == 2

    prices = [9, 9, 9]
    assert solution.max_profit_subtle_two_pointers(prices) == 0

    prices = [7, 6, 4, 3, 1]
    assert solution.max_profit_subtle_two_pointers(prices) == 0


test_max_profit_naive()
test_max_profit_subtle()
print("All tests passed!")
