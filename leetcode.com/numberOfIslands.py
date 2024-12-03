"""
Description:

  200. Number of Islands

  Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
  You may assume all four edges of the grid are all surrounded by water.


  Example 1:
  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1

  Example 2:
  Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  Output: 3

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  1) Starting from top left index, we check if the num is 1, and if it is, we call depth-first-search algorithm.
  2) This algorithm recursively checks the all neighbor cells (horizontally and vertically) and if they are 1, continues recursive calls, and makes them 0 as it goes by.
  3) After checking all neighbors of 1's in the depths of graph, dfs returns back to its caller.
  4) We increment result, and continue with the next index in the loop

Complexities:

  Time: O(n * m) where n is the number of rows, and m is the number of columns (nested for loop)
  Space: O(n  * m), since we have recursive calls, memory will be dominated by call stack, and in the worst case, (all elements of the graph is 1)
  we call function n * m times

Tryouts:

  [
    [1,1,1]
    [1,1,1]
    [1,1,1] ->  [0,0,0]
                [0,0,0]
                [0,0,0]
  ]


"""

from typing import List


class Solution:

    def num_islands(self, grid: List[List[str]]) -> int:

        nRows = len(grid)
        nCols = len(grid[0])

        result = 0

        # We do not need to pass grid, since it can access grid from the enclosing scope
        def dfs(x, y):
            # If I am here, I received coordinates [x,y] which is "1"
            # Base Case
            if x < 0 or x >= nRows or y < 0 or y >= nCols or grid[x][y] == "0":
                return

            grid[x][
                y
            ] = "0"  # Marking it as 0 to indicate that we have visited this island soil

            # Recursive Calls
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for x in range(nRows):
            for y in range(nCols):
                if grid[x][y] == "1":
                    result += 1
                    dfs(x, y)

        return result


def test_num_islands():

    solution = Solution()

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert solution.num_islands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    assert solution.num_islands(grid) == 3

    grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]

    assert solution.num_islands(grid) == 1

    grid = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]

    assert solution.num_islands(grid) == 1


test_num_islands()
print("All tests passed!")
