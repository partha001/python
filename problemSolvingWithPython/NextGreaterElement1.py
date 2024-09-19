#https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size = len(nums1)
        result = [-1] * size

        #defining and populating the map
        #map = dict[int,int]
        map = {}
        for i in range(len(nums1)) :
            map[nums1[i]] = i

        #this will be used as a stack
        stack = []

        for i in range(len(nums2)):
            current = nums2[i]

            while len(stack)!=0 and current > stack[-1]:
                value = stack.pop()
                index = map.get(value)
                result[index] = current
            
            if map.get(current) != None :
                stack.append(current)
        
        return result
    

result = Solution().nextGreaterElement([4,1,2], [1,3,4,2])
print(result)




        