## problem definition: https://leetcode.com/problems/number-of-boomerangs/

from typing import List, Dict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(0,len(points)):
            mydict: Dict[int, int] = {}
            for j in range(0, len(points)):
                if i == j :
                    continue
                key = int(pow(points[i][1]-points[j][1],2)) + int(pow(points[i][0]-points[j][0],2))
                if key in mydict :
                    mydict[key]= mydict.get(key)+1
                else:
                    mydict[key]=1

            for item in mydict:
                result = result + (((mydict.get(item)-1)*(mydict.get(item)))/2)

        return int(result*2)
