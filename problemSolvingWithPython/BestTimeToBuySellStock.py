'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0

        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > buy:
                profit = max(profit, prices[i]- buy)
            buy = min(buy, prices[i])

        return profit
