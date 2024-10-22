#problem statement : https://leetcode.com/problems/non-decreasing-array/
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: # if violates increasing order
                modified+=1
                if modified ==2: # if number of modification reaches threshold
                    return False
                if i<2 or nums[i-2]<=nums[i]: # if its for first 2 element or i-2th element<=ith element
                    nums[i-1] = nums[i] # making the modification at i-1th index
                else:
                    nums[i] = nums[i-1] # making the modification at i-th index

        return True

