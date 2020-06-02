# INPUT:  Only the node to be deleted
# OUTPUT: None (inplace)
# IDEA:   1. Run a pointer from given node to tail node. Copy values from preceeding node to current node.
#         Finally, update the second last node as tail node (next=None) - Keep a variable to point the
#         previous node. (Used here)
#         2. Replace the value of the node we want to delete with the value in the node after it,
#         and then delete the node after it. (Optimized)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node
        prev = node
        while ptr.next is not None:
            ptr.val = ptr.next.val
            prev = ptr
            ptr = ptr.next
        prev.next = None