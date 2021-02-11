#!/usr/bin/env python3

# Title: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Description: Write a function to find the longest common prefix string amongst an array of strings.
#   If there is no common prefix, return an empty string "".
#   Example 1:
#     Input: strs = ["flower","flow","flight"]
#     Output: "fl"
#   Example 2:
#     Input: strs = ["dog","racecar","car"]
#     Output: ""
#     Explanation: There is no common prefix among the input strings.

# Results: Success
#   Runtime: 40 ms, faster than 31.22% of Python3 online submissions for Longest Common Prefix.
#   Memory Usage: 14.4 MB, less than 29.68% of Python3 online submissions for Longest Common Prefix.
from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    try:
      output = strs[0]
    except:
      return("")
    
    for word in strs[1:]:
      # Each word, skipping the first
      letter_i = 0 # word index
      output_tmp = "" # placeholder for next iteration of output
      word_size = len(word)
      for letter in output:
        # Loop through output because it's shorter
        if letter_i < word_size and letter == word[letter_i]:
          # index shouldn't look beyond the size of word
          output_tmp += letter # save letter
        else:
          break #stop looping through output
        letter_i += 1
      output = output_tmp
      
    return(output)
    
          
ans = Solution()
print("Solution: ",ans.longestCommonPrefix(["chicken", "pocop", "duck"]))
print("Solution: ",ans.longestCommonPrefix(["c", "chjghjghj", "c"]))
print("Solution: ",ans.longestCommonPrefix(["chicken", "chipochicop", "chickduckchic"]))
print("Solution: ",ans.longestCommonPrefix(["flower","flow","flight"]))