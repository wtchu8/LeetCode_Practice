#!/usr/bin/env python3

# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#   You may assume that each input would have exactly one solution, and you may not use the same element twice.
#   You can return the answer in any order.
#   Example 1:
#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1]
#     Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#   Example 2:
#     Input: nums = [3,2,4], target = 6
#     Output: [1,2]
#   Example 3:
#     Input: nums = [3,3], target = 6
#     Output: [0,1]
# Constraints:
#   2 <= nums.length <= 103
#   -109 <= nums[i] <= 109
#   -109 <= target <= 109
#   Only one valid answer exists.

# Results: Success
#   Runtime: 40 ms, faster than 95.56% of Python3 online submissions for Two Sum.
#   Memory Usage: 14.4 MB, less than 75.14% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return([i,j])
#Ans=Solution()
#Ans.twoSum([2,7,11,15],9)
