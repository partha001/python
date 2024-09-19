# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        temp = list()
        for index in reversed(range(length)):
            current = temperatures[index]
            while len(temp) and temperatures[temp[-1]] <= current:
                temp.pop()
            
            result[index] = temp[-1]-index if len(temp) else 0
            temp.append(index)
        return result  



solution = Solution()
result = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(result)