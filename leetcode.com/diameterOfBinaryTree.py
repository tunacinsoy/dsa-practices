"""
Description:

  543. Diameter of a Binary Tree

  Given the root of a binary tree, return the length of the diameter of the tree.

  The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

  This path may or may not pass through the root.

  The length of a path between two nodes is represented by the number of edges between them.

  Example 1:

  https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg

  Input: root = [1,2,3,4,5]
  Output: 3


        1
  2         3
4   5


  Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


  Example 2:

  Input: root = [1,2]
  Output: 1

  1
2


Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-03

Version:
    1.0.0

Algorithm Implementation:


Complexities:



Tryouts:

        1
  2         3
4   5



"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_diameter(self, root: TreeNode) -> int:

        if root is None:
            return 0

        result = 0

        # Computes the height of binary tree
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # Retrieve the nonlocal variable result from outer scope
            nonlocal result
            result = max(result, left + right)

            # Think about the leaf node, its left's height is 0, right's height is 0,
            # however it's height should be 1, since it is a node itself
            return max(left, right) + 1

        dfs(root)
        return result


def test_get_diameter():

    solution = Solution()

    # root = [1,2,3,4,5]
    #  1
    # 2  3
    # 4  5
    #

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)

    node1 = TreeNode(1, node2, node3)

    assert solution.get_diameter(node1) == 3

    node2 = TreeNode(2)
    node1 = TreeNode(1, node2, None)
    assert solution.get_diameter(node1) == 1

    pass


test_get_diameter()
print("All tests passed!")
