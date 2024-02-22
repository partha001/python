# https://leetcode.com/problems/jump-game/
# forward moving solution
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        reachable =0
        for i in range(len(nums)):
            if i> reachable:
                return False
            reachable = max( reachable, i + nums[i])
        return True

#backward moving solution    
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastTrue = n-1
        for i in reversed(range(n-1)):
            jumpSize = nums[i]
            if i + jumpSize >= n-1 or i+jumpSize>=lastTrue:
                lastTrue = i
        return lastTrue==0