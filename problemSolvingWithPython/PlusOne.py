'''
https://leetcode.com/problems/plus-one/
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in reversed(range(len(digits))):
            currentDigit = digits[index]
            if currentDigit <9:
                digits[index] = currentDigit +1
                return digits
            else:
                if currentDigit == 9 and index!=0:
                    digits[index] = 0
                else:
                    digits = [0] * (len(digits) +1)
                    digits[0] = 1
        return digits
