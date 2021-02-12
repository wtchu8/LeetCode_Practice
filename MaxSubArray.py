# Poor implemention of https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Loop through all contiguous groups
        # Output the largest sum
        max_total = nums[0]
        # Loop through the list, don't run when first_i is set to the last number
        for first_i in range(len(nums)):
          # Initialize with the first number
          running_total = nums[first_i]

          # Check if just the one number would be the max
          if running_total > max_total:
            max_total = running_total

          if running_total > 0:
            # keep adding to a running total, skip that start point if neg
            for num in nums[first_i+1:]:
              running_total += num
              # Everytime the running total changes, check if it replaces the max
              if running_total > max_total:
                max_total = running_total

        return(max_total)