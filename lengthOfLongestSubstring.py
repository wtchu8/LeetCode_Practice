#!/usr/bin/env python3

# Title: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Description: Given a string s, find the length of the longest substring without repeating characters.
#   Example 1:
#     Input: s = "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with the length of 3.
# Constraints:
#   s consists of English letters, digits, symbols and spaces

# Results: Success
#   Runtime: 6228 ms, faster than 5.02% of Python3 online submissions for Longest Substring Without Repeating Characters.
#   Memory Usage: 14.5 MB, less than 28.23% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def __init__(self):
        self.seen_letters = []
        self.longest_len = 0

    def lengthOfLongestSubstring(self, s: str) -> int:
#       print("string: ",s)
        # for each character count forward until a repeat
            # break if there is a repeat
            # also break once there are less letters remaining than the largest
            # substring
        if len(s) <= 1:
            return(len(s))
 
        self.longest_len = 1
        #Iterate the first letter index
        for first_i in range(len(s)-1):
            # skip if the remaining string is too small to be the largest
            if len(s) - first_i <= self.longest_len:
                break
#           print("first_i: ",first_i)

            # reset list of seen letters
            self.seen_letters = [s[first_i]]
            
            #Iterate through the remainder of the string
            for check_i in range(first_i + 1,len(s)):
#               print("check_i: ",check_i)
                if self.__check_if_seen(s[check_i]):
                    # if there was a match, stop the check loop
                    self.__update_longest_len()
                    break
                else:
                    # if not seen add to list
                    self.seen_letters.append(s[check_i])        
                    if check_i == len(s)-1:
                        #if you hit the end without a match
                        self.__update_longest_len()
        return(self.longest_len)

    def __check_if_seen(self, letter: str) -> bool:
        #Iterate through the seen letters
        for seen_l in self.seen_letters:
            if letter == seen_l:
                return(True)
        return(False)
        
    def __update_longest_len(self):
        if len(self.seen_letters) > self.longest_len:
            self.longest_len = len(self.seen_letters)
#       print("longest_len: ",longest_len)
        
# Test conditions
#ans = Solution()
#print(ans.lengthOfLongestSubstring("abcabcbb"))
#print(ans.lengthOfLongestSubstring("bbbbb"))
#print(ans.lengthOfLongestSubstring("bb"))
#print(ans.lengthOfLongestSubstring("ab"))
