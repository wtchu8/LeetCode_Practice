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
# Results: In Progress

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = self.getNumber(l1)
        x2 = self.getNumber(l2)
        print(x1+x2)

    def getNumber(self, l1: ListNode) -> int:
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
        dig1 = x%10
        rest1 = x//10
        dig2 = rest1%10
        rest2 = rest1//10
        dig3 = rest2%10
        rest3 = rest2//10
        ans = ListNode(dig1,ListNode(dig2,ListNode(dig3)))
    
#print('testing - start')
#x=ListNode(9,ListNode(8,ListNode(7)))
#print(x.next.val)
#print('testing - end')
