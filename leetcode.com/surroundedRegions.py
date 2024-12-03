"""
Description:

  130. Surrounded Regions

  You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

  Connect: A cell is connected to adjacent cells horizontally or vertically.
  Region: To form a region connect every 'O' cell.
  Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
  A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.


  Example 1:
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
    https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg


  Example 2:

    Input: board = [["X"]]

    Output: [["X"]]

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  Key-Point: Call dfs only when the index is in the border of the board. With this approach, dfs will cover
  the entire block of "O"s and convert them into a temporary value "T".

  Q) Why "T"?
  Because we want this field to remain as it is, we should not change them. We should only flip O's which are
  surrounded by X.

  And then, init nested loop, and check if the value is "O" and then convert it to X. And if it is "T", convert it
  back to "O".

Complexities:

  Time: O(n * m) where n is the number of rows, and m is the number of columns (nested for loop)
  Space: O(n  * m), since we have recursive calls, memory will be dominated by call stack, and in the worst case, (all elements of the graph is 1)
  we call function n * m times

Tryouts:

Example 1:
[
  [O,X,O]    [T,X,T]
  [X,O,X] -> [X,O,X]
  [X,X,X]    [X,X,X]

  -> [O,X,O]
     [X,X,X]
     [X,X,X]
]

Example 2:
[
  [O,O,O]    [T,T,T]
  [X,O,X] -> [X,T,X]
  [X,X,X]    [X,X,X]

  -> [O,O,O]
     [X,O,X]
     [X,X,X]
]


"""

from typing import List


class Solution:

    def find_surrounded_regions(self, board: List[List[str]]) -> None:

        if board is None:
            return

        nRow = len(board)
        nCol = len(board[0])

        def dfs(x: int, y: int) -> None:

            # Baseline
            if x < 0 or x >= nRow or y < 0 or y >= nCol or board[x][y] != "O":
                return

            # Change the index to "X"
            board[x][y] = "T"

            # Recursive Calls
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for x in range(nRow):
            for y in range(nCol):
                if board[x][y] == "O" and (
                    x == 0 or x == nRow - 1 or y == 0 or y == nCol - 1
                ):
                    dfs(x, y)

        for x in range(nRow):
            for y in range(nCol):
                if board[x][y] == "O":
                    board[x][y] = "X"

        for x in range(nRow):
            for y in range(nCol):
                if board[x][y] == "T":
                    board[x][y] = "O"


def test_find_surrounded_regions():
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    solution.find_surrounded_regions(board)
    # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


test_find_surrounded_regions()
print("All tests passed!")
