"""

Description:
  122. Best Time to Buy and Sell Stock II

  You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

  On each day, you may decide to buy and/or sell the stock.
  You can only hold at most one share of the stock at any time.
  However, you can buy it then immediately sell it on the same day.

  Find and return the maximum profit you can achieve.

  Examples:

  Input: prices = [7,1,5,3,6,4]
  Output: 7
  Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
  Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
  Total profit is 4 + 3 = 7.


  Input: prices = [7,2,1,3,6,4]
  Output: 7
  Explanation:
  Total profit is 4 + 3 = 7.

  Input: prices = [1,2,3,4,5]
  Output: 4
  Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
  Total profit is 4.

  Input: prices = [7,6,4,3,1]
  Output: 0
  Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-29

Version:
    1.0.0

Algorithm Implementation:
  # KEY POINT
  # When stock prices rise over multiple days,
  # summing the daily increments yields the same profit as buying at the start of the rise and selling at the end.
  # Every time the price rises, we consider it as a potential transaction.

  Subtle Approach:
    prices = [7,1,5,3,6,4]

               f
             b
    [7,1,5,3,6,4]

    profit = 4 + 3 = 7

Complexities:
  Subtle Approach:
    Time: O(n) where n is the length of prices list
    Space: O(1), we only hold one additional variable
"""

from typing import List


class Solution:
    def max_profit_subtle_second(self, prices: List[int]) -> int:

        profit = 0

        # range(1,0) does not throw error, so we do not need to check if len(prices) < 0: return 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit


def test_max_profit_subtle_second():
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    assert solution.max_profit_subtle_second(prices) == 7

    prices = [1, 2, 3]
    assert solution.max_profit_subtle_second(prices) == 2

    prices = [9, 9, 9]
    assert solution.max_profit_subtle_second(prices) == 0

    prices = [7, 6, 4, 3, 1]
    assert solution.max_profit_subtle_second(prices) == 0

    prices = []
    assert solution.max_profit_subtle_second(prices) == 0


test_max_profit_subtle_second()
print("All tests passed!")


for i in range(1, 0):
    print(i)
