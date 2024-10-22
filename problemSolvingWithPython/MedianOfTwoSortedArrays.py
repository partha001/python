# problem statement: https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

import sys


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2) :
            return self.findMedianSortedArrays( nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high :
            midX = (low + high)//2
            midY =  (x + y + 1)//2 - midX

            #if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            #if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            maxLeftX = (-sys.maxsize - 1)  if  (midX == 0) else nums1[midX - 1]
            minRightX = sys.maxsize  if midX==x else nums1[midX]


            maxLeftY = (-sys.maxsize - 1)  if  (midY == 0) else nums2[midY - 1]
            minRightY = sys.maxsize  if midY==y else nums2[midY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # we have partitioned the array at the correct place
                # now we have to median depending upon if its even lenght or odd length
                if (x +y)%2==0 :
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY :  #we are too far on right side for partitionX. Go on left side.
                high = midX - 1
            else: # we are too far on left side for partitionX. Go on right side.
                low = midX + 1;

