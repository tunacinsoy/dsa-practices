"""

Description:
  100. Same Tree

  Given the roots of two binary trees p and q, write a function to check if they are the same or not.

  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

  Examples:

  Input: p = [1,2,3], q = [1,2,3]
  Output: true

  Input: p = [1,2], q = [1,null,2]
  Output: false

  Input: p = [1,2,1], q = [1,1,2]
  Output: false

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-30

Version:
    1.0.0

Algorithm Implementation:

        1           1
      2   3       4   3

Base Cases:
  1) both of the nodes can be None -> ret true
  2) one of them can be None, the other could be not None -> ret False
  3) their values do not match -> ret false

  And if I pass them, I am sure that their values match, and I have node at this iteration in both trees.

Complexities:

  Time: O(n), where n is the count of nodes (We visit each node once, and perform two checks for left and right)

  Space: O(h), where h is the height of the tree.
  Because the call stack will go to the deepest depth, and it will return from there.
  So at the deepest point, the call stack will contain at most h frames, and then gradually return from there.
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """
          1       1
        2   3   2   3
        """
        if p is None and q is None:
            return True
        """
              1         1
                3     2   3


              1         1
            2   3         3
        """
        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        if p.val != q.val:
            return False

        # If I am here, I am sure that in this iteration, I have node in both trees, and their values are same.

        is_left_side_same = self.is_same_tree(p.left, q.left)
        is_right_side_same = self.is_same_tree(p.right, q.right)

        return is_left_side_same and is_right_side_same


def test_is_same_tree():
    solution = Solution()

    # Test Case 1
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1 = TreeNode(1, node2, node3)

    assert solution.is_same_tree(node1, node1) == True

    # Test Case 2
    node4 = TreeNode(2)
    node5 = TreeNode(3)
    node6 = TreeNode(1, node5, node4)

    assert solution.is_same_tree(node1, node6) == False


test_is_same_tree()
print("All tests passed!")
