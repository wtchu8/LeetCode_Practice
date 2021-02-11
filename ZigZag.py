#!/usr/bin/env python3
# Title: ZigZag Conversion
# Link: https://leetcode.com/problems/zigzag-conversion/
# Description: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

#   Example 1:
#     Input: s = "PAYPALISHIRING", numRows = 4
#     Output: "PINALSIGYAHRPI"
#     Explanation:
#     P     I    N
#     A   L S  I G
#     Y A   H R
#     P     I


# Results: Success
#   Runtime: 64 ms, faster than 54.25% of Python3 online submissions for ZigZag Conversion.
#   Memory Usage: 14.5 MB, less than 48.19% of Python3 online submissions for ZigZag Conversion.

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    s_size=len(s)
    # go through each element and place in the appropriate list
    # list of strings used for storage
    full_out = ""
    out=[]
    cycle_size = numRows+(numRows-2)

    # Handle edge case of numRows = 1
    if numRows == 1:
        cycle_size = 1

    # initialize list of strings
    for j in range(cycle_size):
        out.append("")

    for i in range(s_size):
#      print(s[i],i)
      
      if (i % cycle_size) == 0:
        #restart cycle
#        print("restart cycle")
        set_i = 0 # value within cycle
        diag_i = 1 # value within diagonal

      if set_i >= numRows:
        # letter in diagonal
#        print("diag",numRows-diag_i-1)
        list_i = numRows-diag_i-1
        diag_i += 1
      else:
#        print("vert")
        list_i = set_i
        # letter in vertical
        # append letter to the correct list
      out[list_i] += s[i]
        
      set_i += 1

    #Concatenate list of strings and output
    for str_i in out:
#      print(str_i)
      full_out += str_i
    return(full_out)

ans = Solution()
print(ans.convert("abcdefghijklmn",1))
print(ans.convert("a",1))