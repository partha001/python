#https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [None] * n
        for i in range(n):
            temp[(i+k)%n] = nums[i]
        
        for i in range(n):
            nums[i] = temp[i]

        