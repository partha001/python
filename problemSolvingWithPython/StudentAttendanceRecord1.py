'''
https://leetcode.com/problems/student-attendance-record-i/
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCount = 0
        consecutiveLateCount = 0
        for c in s:
            consecutiveLateCount = 0 if c!='L' else consecutiveLateCount+1

            if c=='A':
                absentCount +=1

            if consecutiveLateCount>=3 or absentCount==2:
                return False

        return True