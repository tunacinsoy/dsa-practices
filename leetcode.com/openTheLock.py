"""
Description:

  752. Open the Lock

  You have a lock in front of you with 4 circular wheels.
  Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
  The wheels can rotate freely and wrap around:
  for example we can turn '9' to be '0', or '0' to be '9'.
  Each move consists of turning one wheel one slot.

  The lock initially starts at '0000', a string representing the state of the 4 wheels.

  You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
  the wheels of the lock will stop turning and you will be unable to open it.

  Given a target representing the value of the wheels that will unlock the lock,
  return the minimum total number of turns required to open the lock, or -1 if it is impossible.

  Example 1:
  Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
  Output: 6
  Explanation:
  A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
  Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
  because the wheels of the lock become stuck after the display becomes the dead end "0102".

  Example 2:
  Input: deadends = ["8888"], target = "0009"
  Output: 1
  Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

  Example 3:
  Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
  Output: -1
  Explanation: We cannot reach the target without getting stuck.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-04

Version:
    1.0.0

Algorithm Implementation:



Complexities:



Tryouts:


                         "0000"

"1000", "9000"; "0100", "0900"; "0010", "0090"; "0001", "0009"; (we have 8 children for each breadth)



"""

from typing import List
from collections import deque


class Solution:
    def open_lock(self, deadends: List[str], target: str) -> int:

        # If init position is in deadends, then we cannot proceed further
        if "0000" in deadends:
            return -1

        # We will apply bfs, so let's implement deque
        queue = deque()

        # We do not want deadends to be visited
        visited = set(deadends)

        def get_children(key: str) -> List[str]:
            #       0000
            # "1000", "9000"; "0100", "0900"; "0010", "0090"; "0001", "0009"; (we have 8 children for each breadth)
            # 9 + 1 = 10 % 10 = 0
            #
            res = []

            for i in range(len(key)):

                # Retrieve digit, add 1, and then take mod 10, and we have the updated digit
                digit = str((int(key[i]) + 1) % 10)

                # key has to remain the same, since we will iterate over it. That's why,
                # we need to do append operation like this.

                # 0000 -> 0010 -> 00 + 1 + 0 = 0010
                res.append(key[:i] + digit + key[i + 1 :])

                # For -1 case, we need to add 10 and take modulo 10 (-1 + 10 = 9; 9 mod 10 = 9)
                digit = str((int(key[i]) - 1 + 10) % 10)

                res.append(key[:i] + digit + key[i + 1 :])

            return res

        queue.append(
            ["0000", 0]
        )  # The key that we are currently in, and how many moves did we do to reach this key?

        while len(queue) > 0:

            key, moves = queue.popleft()

            # If we happen to be at target position, we can return num of moves
            if key == target:
                return moves

            curr_key_children = get_children(key)
            for child in curr_key_children:
                if child not in visited:
                    queue.append([child, moves + 1])
                    visited.add(child)

        return -1


def test_open_lock():
    # Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"

    solution = Solution()

    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    assert solution.open_lock(deadends, target) == 6

    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"

    assert solution.open_lock(deadends, target) == -1

    deadends = ["8888"]
    target = "0009"

    assert solution.open_lock(deadends, target) == 1


test_open_lock()

print("All tests passed!")
