'''
https://leetcode.com/problems/squares-of-a-sorted-array/
'''
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums)-1
        index = len(nums)-1

        while left < len(nums) and right>=0 and left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[index] = (nums[left] * nums[left])
                left+=1
            else:
                result[index] = (nums[right] * nums[right])
                right-=1
            index-=1

        return result

