#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = [None] * len(nums)
        left : int = 1
        length : int = len(nums)
        for i in range(length):
            result[i] = left
            left = left * nums[i]
        
        right : int = 1
        for i in reversed(range(length)):
            result[i] = result[i] * right
            right = right * nums[i]
        
        return result