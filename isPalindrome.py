#!/usr/bin/env python3

# Title: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Description: Given an integer x, return true if x is palindrome integer.
#   An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#   Example 1:
#     Input: x = 121
#     Output: true
#   Example 2:
#     Input: x = -121
#     Output: false
#     Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Results: Success
#   Runtime: 56 ms, faster than 83.57% of Python3 online submissions for Palindrome Number.
#   Memory Usage: 14.2 MB, less than 80.32% of Python3 online submissions for Palindrome Number.

class Solution:
  def isPalindrome(self, x: int) -> bool:
    # Function: return True if it is a Palindrome, else return false
    
    print("---",x,"---")
    # Handle negative edge case
    if x < 0:
      return(False)
    # Split the integer into an list, one digit per element
      # Convert to a string
    x_str = str(abs(x))
    x_len = len(x_str)
    # if odd will round down, else will check half of digits 
    i_check = x_len // 2
    
    # Check that the first digit matches the last and so on
    #   until you reach the middle point
    #   handle odd vs. even number of digits implementation
    #   If there is any unmatched number, break and return false
    for i in range(0,i_check):
      i_opposite = x_len - 1 - i
      if x_str[i] != x_str[i_opposite]:
        return False
    
    #If passed through entire for loop, return True
    return True

ans = Solution()
print(ans.isPalindrome(124421))
print(ans.isPalindrome(1245421))
print(ans.isPalindrome(148541))
print(ans.isPalindrome(1245471))

print(ans.isPalindrome(124421))
print(ans.isPalindrome(1245421))
print(ans.isPalindrome(148541))
print(ans.isPalindrome(-1245471))
