"""

Description:
  101. Symmetric Tree

  Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

  Examples:

  Input: root = [1,2,2,3,4,4,3]
  Output: true

  Input: root = [1,2,2,null,3,null,3]
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

        1
  2           2
3   4       4   3


  1) left is none and right is none -> ret true

  # If I am here, there are two conditions to check:
    first: both of them is not none -> condition that i want to have (to check their values later)
    second: one of them is none, and the other is not none -> false condition

  2) left is none or right is none -> ret false




Complexities:

  Time: O(n), where n is the count of nodes (We visit each node once, and perform two checks for left and right)

  Space: O(h), where h is the height of the tree.
  Because the call stack will go to the deepest depth, and it will return from there.
  So at the deepest point, the call stack will contain at most h frames, and then gradually return from there.
"""

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetrical(self, root: TreeNode) -> bool:
        """
            1

        2      3
        """
        if root is None:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left_node: TreeNode, right_node: TreeNode) -> bool:

        # Base Cases
        if left_node is None and right_node is None:
            return True

        if left_node is None or right_node is None:
            return False

        # If I am here, I am sure that there are nodes to compare

        if left_node.val == right_node.val:
            # If I am here, current iteration's checks are complete, I need to go on

            left_right_check = self.is_mirror(left_node.left, right_node.right)
            right_left_check = self.is_mirror(left_node.right, right_node.left)

            return left_right_check and right_left_check

        # Values do not match, return False
        else:
            return False


class TestIsSymmetrical(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_symmetric_tree(self):
        # Symmetric tree
        #     1
        #    / \
        #   2   2
        #  / \ / \
        # 3  4 4  3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(self.solution.is_symmetrical(root))

    def test_asymmetric_tree(self):
        # Asymmetric tree
        #     1
        #    / \
        #   2   2
        #    \   \
        #     3    3
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(3))
        root.right = TreeNode(2, None, TreeNode(3))
        self.assertFalse(self.solution.is_symmetrical(root))

    def test_empty_tree(self):
        # Empty tree
        self.assertTrue(self.solution.is_symmetrical(None))

    def test_single_node(self):
        # Single node tree
        root = TreeNode(1)
        self.assertTrue(self.solution.is_symmetrical(root))


if __name__ == "__main__":
    unittest.main()

# test_is_symmetrical()
# print("All tests passed!")
