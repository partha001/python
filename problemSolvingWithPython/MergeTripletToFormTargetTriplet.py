#https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = set()
        for i in range(len(triplets)):
            currentTriplet = triplets[i]
            #print(type(currentTriplet))
            if currentTriplet[0]>target[0] or currentTriplet[1]>target[1] or currentTriplet[2]> target[2]:
                continue
            for j in range(3):
                if(currentTriplet[j]== target[j]):
                    result.add(j)
        
        return len(result)==3