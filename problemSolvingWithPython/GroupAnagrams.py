#problem statement: https://leetcode.com/problems/group-anagrams/
from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict: Dict[str, list[str]] = {}
        result : list[list[str]] = []
        for item in strs:
            mylist = list(item)
            mylist.sort()
            key = "".join(mylist)
            print(key)
            if mydict.get(key) != None:
                mydict[key].append(item)
            else:
                mydict[key] = [item]

        for key in mydict.keys():
            result.append(mydict[key])

        return result
