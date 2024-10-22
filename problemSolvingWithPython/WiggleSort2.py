# problem statement : https://leetcode.com/problems/wiggle-sort-ii/

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        #sorting the input
        nums.sort()

        #find mid point of the list
        mid = int((len(nums)-1)/2)
        right = len(nums)-1

        #aux list to temp store the values
        result = [0] * (right +1)
        counter = 0

        # select values from two parts of the list and arrange them in aux array
        while mid >=0 or right > ((len(nums)-1)/2) :

            if counter %2 ==0:
                result[counter] = nums[mid]
                mid-=1
            else:
                result[counter] = nums[right]
                right-=1

            counter+=1


        #now store back these values in input/original array
        for i in range (0, len(nums)):
            nums[i] = result[i]






