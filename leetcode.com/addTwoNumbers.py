"""
Description:

  2. Add Two Numbers

  You are given two non-empty linked lists representing two non-negative integers.
  The digits are stored in reverse order, and each of their nodes contains a single digit.
  Add the two numbers and return the sum as a linked list.

  You may assume the two numbers do not contain any leading zero, except the number 0 itself.


  Example 1:
  https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

  Input: l1 = [2,4,3], l2 = [5,6,4]
  Output: [7,0,8]
  Explanation: 342 + 465 = 807.

  Example 2:
  Input: l1 = [0], l2 = [0]
  Output: [0]

  Example 3:

  Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
  Output: [8,9,9,9,0,0,0,1]

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-02

Version:
    1.0.0

Algorithm Implementation:


Complexities:

    Time :  O(max(n, m)), where n is the number of nodes of l1, and m is the number of nodes in l2
    Space:  O(max(n, m)), where n is the number of nodes of l1, and m is the number of nodes in l2

Tryouts:

Input: l1 = [2,4,3], l2 = [5,6,4]

multiplier = 1
num = 2 + 40 + 300 = 342

          p
2 -> 4 -> 3

"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_number(self, head: ListNode) -> int:

        multiplier = 1
        sum = 0

        while head != None:
            sum += int(head.val) * multiplier
            head = head.next
            multiplier *= 10

        return sum

    def construct_linked_list(self, sum: int) -> ListNode:
        if sum == 0:
            return ListNode(0)

        dummy = ListNode()
        current = dummy

        while sum > 0:
            current.next = ListNode(sum % 10)
            sum //= 10
            current = current.next

        return dummy.next

    def addTwoNumbers(self, l1, l2) -> List[ListNode]:

        sum1 = self.get_number(l1)
        sum2 = self.get_number(l2)

        return self.construct_linked_list(sum1 + sum2)


def test_add_two_numbers():
    solution = Solution()

    # Test Case #1
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    node2 = ListNode(2)
    node4 = ListNode(4)
    node3 = ListNode(3)

    node2.next = node4
    node4.next = node3

    node5 = ListNode(5)
    node6 = ListNode(6)
    node44 = ListNode(4)

    node5.next = node6
    node6.next = node44

    sum_ll = solution.addTwoNumbers(node2, node5)

    # To check the values of linked list
    while sum_ll != None:
        print(sum_ll.val, end=" -> ")
        sum_ll = sum_ll.next
    print()


test_add_two_numbers()
