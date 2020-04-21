# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self,binaryMatrix : 'BinaryMatrix') -> int:
        len_row,len_col=binaryMatrix.dimensions()
        row=0
        col=len_col-1
        res=-1
        while row<len_row and col>=0:
            if binaryMatrix.get(row,col)==1:
                res=col
                col-=1
            else:
                row+=1
        return res        
        
        