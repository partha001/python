'''
https://leetcode.com/problems/maximum-product-subarray/
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        mpp = nums[0] #max-positive-product
        mnp = nums[0] #max-negative-product
        mop = nums[0] #max-overall-product

        for i in range(1,len(nums)):
            current = nums[i]
            if current>=0:
                mpp = max(current, current * mpp)
                mnp = min(current , current * mnp)
            else:
                temp1 = mpp
                temp2 = mnp
                mpp = max(current, current * temp2)
                mnp = min(current, current * temp1)
            mop = max(mop, mpp)

        return mop
