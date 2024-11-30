"""

Description:
  226. Invert Binary Tree

  Given the root of a binary tree, invert the tree, and return its root.

  Examples:

  Input: root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

            4
      2             7
  1     3         6    9


            4
    7               2
  9     6         3    1


  Input: root = [2,1,3]
  Output: [2,3,1]

  Input: root = []
  Output: []

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-30

Version:
    1.0.0

Algorithm Implementation:

  For each root, swap its left and right child node


    #           4
    #     2             7
    # 1     3         6    9

    #           4
    #     7             2
    # 9     6         3    1

    tree_node_list = [4,7, 2]
    queue= [2,9,6]


Complexities:

  Time: O(n), where n is the count of nodes (We visit each node once, and perform two checks for left and right)

  Space: O(h), where h is the height of the tree.
  Because the call stack will go to the deepest depth, and it will return from there.
  So at the deepest point, the call stack will contain at most h frames, and then gradually return from there.
"""

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:

        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root

    def nodes_in_list_preorder(self, root: TreeNode) -> List[TreeNode]:

        tree_node_list = []

        # Node, Left, Right
        def preorder(node):
            if node is None:
                return
            tree_node_list.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return tree_node_list

    def nodes_in_list_bfs(self, root: TreeNode) -> List[int]:

        tree_node_list = []

        if root is None:
            return tree_node_list

        double_ended_queue = deque([root])

        while len(double_ended_queue) != 0:

            node = double_ended_queue.popleft()
            tree_node_list.append(node.val)

            if node.left is None:
                continue
            if node.right is None:
                continue

            double_ended_queue.append(node.left)
            double_ended_queue.append(node.right)

        return tree_node_list


def test_invert_tree():
    solution = Solution()
    #           4
    #     2             7
    # 1     3         6    9

    #           4
    #     7             2
    # 9     6         3    1

    #     1
    # 2       3
    # queue = []
    # tree_node_list = [1, 2, 3]

    # Test Case #1
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)

    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)

    node4 = TreeNode(4, node2, node7)

    root = solution.invert_tree(node4)

    # Prints in preorder, node's val, left, and right
    nodes_list = solution.nodes_in_list_preorder(root)
    assert nodes_list == [4, 7, 9, 6, 2, 3, 1]

    # Prints in breadth-first search, prints each depth and then proceeds with node.left
    nodes_list = solution.nodes_in_list_bfs(root)
    assert nodes_list == [4, 7, 2, 9, 6, 3, 1]


test_invert_tree()
print("All tests passed!")
