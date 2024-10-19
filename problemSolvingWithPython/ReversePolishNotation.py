from typing import List

### problem statement : https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mylist = []
        for token in tokens :
            if token == "+" or token=="-" or token=="*" or token=="/":
                val1 = mylist.pop()
                val2 = mylist.pop()
                if token == "+":
                    mylist.append(val2+val1)
                elif token == "-":
                    mylist.append(val2 - val1)
                elif token == "*":
                    print(val2 , val1)
                    mylist.append(val2 * val1)
                elif token == "/":
                    mylist.append(int(val2 / val1))
            else:
                mylist.append(int(token))
        return mylist.pop()
