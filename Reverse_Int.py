#!/usr/bin/env python3

# Title: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Description:
#   Given a signed 32-bit integer x, return x with its digits reversed.
#   If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#   Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Ex. -123 --> -321

# Results: Success
# Runtime: 64 ms, faster than 5.01% of Python3 online submissions for Reverse Integer.
#   Runtime might be improved by converting the array to a string to an array of characters, then reverse order
# Memory Usage: 14.1 MB, less than 91.51% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:

        print('x: ',x)
        
        #Remove sign
        if x < 0:
            is_neg=True
            x=-1*x
        else:
            is_neg=False

        #Place the digits in an array
        dig_list=[]
        while True:
            remainder = x % 10
            #Adding to the end of the list
            dig_list.append(remainder)
            if x < 10:
                    break
            x = x // 10
        print(dig_list)

        #Recombine the digits to a number
        result=0
        for y in dig_list:
            result=(result*10)+y
        #add back sign if needed
        if is_neg == True:
            result=-1*result

        if result > (2**31) - 1 or result < -2**31:
            print('result: ',0)
            return 0
        else:
            print('result: ',result)
            return result
