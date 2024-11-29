"""

Description:
  104. Maximum Depth of Binary Tree

  Given the root of a binary tree, return its maximum depth.

  A binary tree's maximum depth is the number of nodes along the
  longest path from the root node down to the farthest leaf node.

  Examples:

  Input: root = [3,9,20,null,null,15,7]
  Output: 3

  Input: root = [1,null,2]
  Output: 2

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-30

Version:
    1.0.0

Algorithm Implementation:

         3
    9         20
            15   7

        1
            2


3 -> 9 max(root.left = 0, root.right = 0) + 1
3 -> (root.left = 1)

3 -> 20 (root.right = 2) -> 15 max(root.left = 0, root.right = 1) + 1 -> 7 max(root.left = 0, root.right = 0) + 1
3 -> max(root.left = 1, root.right = 2) + 1 = 3

Complexities:

  Time: O(n), where n is the count of nodes (We visit each node once, and perform two checks for left and right)

  Space: O(h), where h is the height of the tree.
  Because the call stack will go to the deepest depth, and it will return from there.
  So at the deepest point, the call stack will contain at most h frames, and then gradually return from there.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max_depth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        left_depth = self.get_max_depth(root.left)
        right_depth = self.get_max_depth(root.right)

        return max(left_depth, right_depth) + 1


def validate_get_max_depth():

    solution = Solution()

    # Test Case 1
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)

    node9 = TreeNode(9)
    node3 = TreeNode(3, node9, node20)

    assert solution.get_max_depth(node3) == 3

    # Test Case 2
    node2 = TreeNode(2)
    node1 = TreeNode(1, None, node2)

    assert solution.get_max_depth(node1) == 2


validate_get_max_depth()
print("All tests passed!")
