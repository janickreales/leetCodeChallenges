# https://leetcode.com/problems/subrectangle-queries/

import numpy as np

class SubrectangleQueries(object):

    def __init__(self, rectangle):
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rectangle[i][j]=newValue
        return f'subrectangleQueries.updateSubrectangle() :\n{np.array(self.rectangle)}'
        

    def getValue(self, row, col):
        return f'subrectangleQueries.getValue({str(row)},{str(col)}) : {self.rectangle[row][col]}'
    
    def __str__(self):
        return f'Initial rectangle: \n{np.array(self.rectangle)}'
    


rect1 = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(rect1)
print(rect1.getValue(*[0,2]))
print(rect1.updateSubrectangle(*[0,0,3,2,5]))
print(rect1.getValue(*[0,2]))
print(rect1.getValue(*[3,1]))
print(rect1.updateSubrectangle(*[3,0,3,2,10]))
print(rect1.getValue(*[3,1]))