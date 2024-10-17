## problem statement: https://leetcode.com/problems/valid-sudoku

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = set()
        squareSet = set()

        for i in range(0,len(board)):
            for j in range(0, len(board[i])):
                value = board[i][j]
                if value == ".":
                    continue
                else:
                    rowString = "row:{}-value:{}".format(i,value)
                    colString = "col:{}-value:{}".format(j,value)
                    squareString = "x:{}-y:{}-value:{}".format(int(i/3),int(j/3),value)
                    print(rowString, colString, squareString)
                    if rowString in rowSet :
                        return False
                    else:
                        rowSet.add(rowString)

                    if colString in colSet :
                        return False
                    else:
                        colSet.add(colString)

                    if squareString in squareSet :
                        return False
                    else:
                        squareSet.add(squareString)
        return True


