#problem statement: https://leetcode.com/problems/largest-number/
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # use custom sort comparison to order numbers in descending order by most significant degit
        # [3,30,34,5,9] -> [9,5,34,3,30]
        # can compare pairs of nums at a time; try each concatenation order and the order should be
        # the concatenation order that produces a greater number
        # ex: 330 vs. 303 -> 3 then 30

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        # convert nums to list of strings for easy concatenation
        nums_s = [str(num) for num in nums]
        nums_s = sorted(nums_s, key=cmp_to_key(compare))
        # if first element is 0, they must all be 0 due to sort; the res should not have leading 0s
        if nums_s[0] == '0':
            return "0"
        return "".join(nums_s)