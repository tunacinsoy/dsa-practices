"""
Description:

  909. Snakes and Ladders

  You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style
  starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

  You start on square 1 of the board. In each move, starting from square curr, do the following:

    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
    This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
    The game ends when you reach the square n2.
    A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c].
    Squares 1 and n^2 are not the starting points of any snake or ladder.

  Note that you only take a snake or ladder at most once per dice roll.
  If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

  For example, suppose the board:   [
                                     [-1,4],
                                     [-1,3]
                                    ],

  and on the first move, your destination square is 2.
  You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

  Return the least number of dice rolls required to reach the square n^2. If it is not possible to reach the square, return -1.


  Example 1:

  https://assets.leetcode.com/uploads/2018/09/23/snakes.png

  Input:
  board = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
           ]

  Output: 4

  Explanation:
  In the beginning, you start at square 1 (at row 5, column 0).
  You decide to move to square 2 and must take the ladder to square 15.
  You then decide to move to square 17 and must take the snake to square 13.
  You then decide to move to square 14 and must take the ladder to square 35.
  You then decide to move to square 36, ending the game.
  This is the lowest possible number of moves to reach the last square, so return 4.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-03

Version:
    1.0.0

Algorithm Implementation:
    Breadt-First Search:
        1) Init deque and set for bfs and keep tracking of visited cells, respectively.
        2) Add the first cell to deque, and to visited set
        3) While there is an item in the queue, pop from left, and implement for loop with dice
        4) If the arrived point is dim * dim, return True, since we finished the game
        5) Implement cell_value_to_row_column_index function, key points are:
            for row calculation -> (cell - 1) // dimension
            for column calculation -> (cell - 1) % dimension
        However, we need to do extra operation for the Boustrophedon style.
        6) If the val of the index arrived at that position is not -1, (meaning that we have snake or ladder) make next_cell the value of that cell
        7) If the position is not visited before, add it to the visited set
        8)


        for row calculation -> (cell - 1) // dimension -> gives the zero-based row index from the top.
        for column calculation -> (cell - 1) % dimension -> gives the zero-based column index from the left.

Complexities:
    Time: O(n) where n is the total number of cells, since we visit each cell only once. For each cell, we consider up to 6 moves.
    Space: O(n) we will have a set to keep track of visited cells, and a deque to store outcomes. Each cell will be in deque at most 1 time.

Tryouts:

"""

from typing import List, Tuple
from collections import deque


class Solution:
    def get_least_rolls(self, board: List[List[int]]) -> int:

        # n*n square board
        dim = len(board)

        # To track if the current cell is visited or not
        visited = set()

        # Double-ended queue, used for bfs implementation
        queue = deque()

        # We will add the (current cell, number of moves to come here) as first element of the queue
        queue.append((1, 0))

        # We visited the first cell, so we also need to add it into set as well
        visited.add((1, 0))

        def num_to_pos(cell_num: int) -> Tuple[int, int]:
            """
            The row index will not change, even though the sequence of numbers are in
            Boustrophedon style. Only the columns need to be adjusted.

            16  15   14  13
             9  10   11  12
             8   7    6   5
             1   2    3   4

             8 -> [2][0]
             2 -> [3][1]

            """

            # (cell_num - 1) // dim -> gives the zero-based row index from the top.
            # Subtracting from dim - 1 flips the index to count from the bottom.
            row = (dim - 1) - (cell_num - 1) // dim

            # If the dim is 4, the last index of each row is going to be (4*k - 1) where k >= 1
            col = (cell_num - 1) % dim

            # If the row is even when counted from the bottom ((dim - row) % 2 == 0),
            # reverse the column index to account for the serpentine order.
            if (dim - row) % 2 == 0:
                col = dim - 1 - col

            return row, col

        # While there are elements in our queue (meaning that there are still paths to discover)
        while len(queue) > 0:

            # Retrieving the first element from the queue
            curr, moves = queue.popleft()

            # If we are on the last cell
            if curr == dim * dim:
                return moves

            # We will keep on dicing until we reach the end point, and the dice has values [1,6]
            # so, curr + 1 is the next closest cell, and min(curr + 6, dim * dim) + 1 is the farthest cell (+1 because of inclusivity)
            # if curr, moves = (1,0) then range becomes (2,8). Remember, 8 is not included in the range.
            for next_cell in range(curr + 1, min(curr + 6, dim * dim) + 1):
                # We have a next_square value (like 25 for instance) and we want to convert it into matrix dimensions
                r, c = num_to_pos(next_cell)

                # We have a snake or ladder on the next_square, so we need to follow it
                if board[r][c] != -1:
                    next_cell = board[r][c]

                # If we are on a cell that was not visited before
                if next_cell not in visited:
                    # Add the cell into visited set
                    visited.add(next_cell)
                    # And add the values to queue ( for instance -> (25,5): meaning that I am on 25th cell, and I came here after 5 steps)
                    queue.append((next_cell, moves + 1))

        return -1


def test_get_least_rolls():
    solution = Solution()
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]

    assert solution.get_least_rolls(board) == 4
    print("All tests passed!")


test_get_least_rolls()
