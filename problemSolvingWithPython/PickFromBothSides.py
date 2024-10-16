# pproblem statement: https://www.interviewbit.com/problems/pick-from-both-sides/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        currentSum =0
        result = 0
        for index in range(0,B):
            currentSum  = currentSum + A[index]

        result = currentSum
        rightIndex = B-1
        leftIndex = len(A)-1
        for index in range(0, B):
            currentSum = currentSum -  A[rightIndex - index] + A[leftIndex-index]
            result = max(result , currentSum)

        return result