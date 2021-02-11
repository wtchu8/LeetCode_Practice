#!/usr/bin/env python3

# Title: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Description: You are given two non-empty linked lists representing two non-negative integers.
#   The digits are stored in reverse order, and each of their nodes contains a single digit.
#   Add the two numbers and return the sum as a linked list.
#   You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#   Example 1:
#     Input: l1 = [2,4,3], l2 = [5,6,4]
#     Output: [7,0,8]
#     Explanation: 342 + 465 = 807.
# Results: Success
#   Runtime: 112 ms, faster than 5.01% of Python3 online submissions for Add Two Numbers.
#   Memory Usage: 14.4 MB, less than 12.35% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Runs addition operation of two ListNodes
        x1 = self.getNumber(l1)
        x2 = self.getNumber(l2)
        return(self.numToListNode(x1+x2))

    def getNumber(self, l1: ListNode) -> int:
        # Function converts a ListNode to a number
        total = 0
        pow = 1
        li = l1
        while True:
            total += ( li.val * pow )
            next_list=li.next
            if next_list == None:
                break
            else:
                li = next_list
                pow *= 10
        return(total)
    
    def numToListNode(self, x: int) -> ListNode:
        # Function converts a number to a ListNode
        first_iteration = True
        # Converting to a string and iterating through string goes first to last digit
        for dig in str(x):
            # On first iteration, initialize node with no next
            if first_iteration == True:
                out_ListNode = ListNode(dig)
            else:
                out_ListNode = ListNode(dig,out_ListNode)
            first_iteration = False
        return(out_ListNode)
