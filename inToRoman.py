#!/usr/bin/env python3

# Title: Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/
# Description: Given an integer, convert it to a roman numeral.
# Constraints:
#   1 <= num <= 3999

# Results: Success
#   Runtime: 64 ms, faster than 20.57% of Python3 online submissions for Integer to Roman.
#   Memory Usage: 14.3 MB, less than 31.43% of Python3 online submissions for Integer to Roman.

class Solution:
  def inToRoman(self, num: int) -> str:
    # Convert an integer into roman numerals
    # for numbers between 1 and 3999
    
    # Initialize output string
    ans = str()

    # Define symbol value conversion manually in dict
    roman_d = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC",
              50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

     # Take the largest symbol or symbol combo (subtraction rules)
      # that is less than x and subtract it from x
      # append that symbol to the string until x is 0    
    while num > 0:
      # Find the largest key that is less than num
      for key in list(roman_d.keys()):
        if key <= num:
          num -= key
          ans += str(roman_d[key])
          break
          
    return(ans)

derp = Solution()
print(derp.inToRoman(444))
