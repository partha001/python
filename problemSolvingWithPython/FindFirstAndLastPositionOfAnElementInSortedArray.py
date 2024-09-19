#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==0:
            return [-1,-1]

        found = self.search(nums, target, 0, len(nums)-1)
        if found==-1:
            return [-1,-1]

        left = found
        right = found

        while left>=0 and  found!=-1:
            found = self.search(nums, target, 0, left-1)
            left = found if found!=-1 else left
        
        found = right
        while right<len(nums) and found!=-1:
            found = self.search(nums, target, right+1, len(nums)-1)
            right = found if found!=-1 else right
            
        return [left, right]



    def search(self, nums: List[int], target:int , start:int , end:int) -> int:       
        if start>end:
            return -1
        mid = int((start +end)/2)
        if nums[mid]==target:
            return mid
        
        if target <= nums[mid]:
            return self.search(nums, target, start, mid-1)
        return self.search(nums, target, mid+1, end)
    



solution = Solution()
result = solution.searchRange([1],1) 
print(result)