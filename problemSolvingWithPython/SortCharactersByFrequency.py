#https://leetcode.com/problems/sort-characters-by-frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        #first we create a dictionary and find all the frequencies
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        st = ""
        #we iterate through the dictionary items where it is sorted by value 
        #sorting is done in ascending order
        for i in sorted(dic.items(), key=lambda x:x[1]):
            # print(i)
            #then we add the character by multiplying item*frequency
            st += i[0] * i[1]
        # print(st)
        #as the sorting is done in ascending order we reverse the string for output
        return st[::-1]
        