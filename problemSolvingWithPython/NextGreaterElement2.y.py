#https://leetcode.com/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [-1] * length
        stack = [] #this will be the stack

        for i in range(length*2):
            index = i % length

            while len(stack)!=0 and nums[stack[-1]] < nums[index]:
                top = stack.pop()
                result[top] = nums[index]

            stack.append(index)

        return result

