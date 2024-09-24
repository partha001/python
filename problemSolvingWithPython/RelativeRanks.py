'''
https://leetcode.com/problems/relative-ranks/
'''
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        mydict = {}
        for index in range(len(score)):
            if index ==0:
                mydict[sortedScore[index]] ="Gold Medal"
            elif index == 1:
                mydict[sortedScore[index]] = "Silver Medal"
            elif index ==2:
                mydict[sortedScore[index]] = "Bronze Medal"
            else:
                mydict[sortedScore[index]] = str(index+1)

        res = []
        for i in score:
            res.append(mydict[i])
        return res


solution = Solution()
print(solution.findRelativeRanks([5,4,3,2,1]))
print(solution.findRelativeRanks([10,3,8,9,4]))



