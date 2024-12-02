"""
Description:

  141. Linked List Cycle

  Given head, the head of a linked list, determine if the linked list has a cycle in it.

  There is a cycle in a linked list if there is some node in the list that can be reached again
  by continuously following the next pointer.

  Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
  Note that pos is not passed as a parameter.

  Return true if there is a cycle in the linked list. Otherwise, return false.


  Note that:

  The valid operators are '+', '-', '*', and '/'.
  Each operand may be an integer or another expression.
  The division between two integers always truncates toward zero.
  There will not be any division by zero.
  The input represents a valid arithmetic expression in a reverse polish notation.
  The answer and all the intermediate calculations can be represented in a 32-bit integer.

  Example 1:
  https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
  Input: head = [3,2,0,-4], pos = 1
  Output: true
  Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

  Example 2:
  https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
  Input: head = [1,2], pos = 0
  Output: true
  Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

  Example 3:
  https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png
  Input: head = [1], pos = -1
  Output: false
  Explanation: There is no cycle in the linked list.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:

  Implementation with additional field in Node:
    1) Iterate over linked list, (until node.next != None) and with each node visit, check the node.isVisited
    2) If it is true, then return true
    3) If it is false, continue with node.next
    4) If out of the while loop, return false

  Floyd's Tortoise and Hare algorithm:
    This algorithm uses two pointers that move at different speeds.
    If there is a cycle, the fast pointer (hare) will eventually meet the slow pointer (tortoise).


Complexities:

    Time :  O(n), where n is the number of nodes
    Space:  O(n), since we use one additional field for each node

Tryouts:

        l     r
   1 -> 2 <-> 3

   1 <-> 2

"""


class ListNode:
    def __init__(self, val=0, next=None, is_visited=False):
        self.val = val
        self.next = next
        self.is_visited = is_visited


class Solution:
    def has_cycle(self, head: ListNode) -> bool:

        if head == None:
            return False

        while head.next != None:
            if head.is_visited == True:
                return True
            else:
                head.is_visited = True
                head = head.next

        return False

    def has_cycle_floyd(self, head: ListNode) -> bool:

        if head == None:
            return False

        slow = head
        fast = head

        while fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def test_has_cycle():

    solution = Solution()

    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node2

    assert solution.has_cycle(node1) == True

    node1.next = node2
    node2.next = node3
    node3.next = None

    assert solution.has_cycle_floyd(node1) == False


test_has_cycle()

print("All tests passed!")
