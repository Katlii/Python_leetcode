#Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        res += matrix.pop(0)
        while matrix and matrix[0]:
            if matrix[0]:
                for i in range(len(matrix)):
                    res.append(matrix[i].pop())
            matrix=matrix[::-1]
            if matrix[0]:
                res=res+matrix[0][::-1]
                matrix.pop(0)
            if matrix:
                for i in range(len(matrix)):
                    matrix[i]=matrix[i][::-1]
        return res


"""import numpy as np
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix[0])
        m=len(matrix)
        matrix=np.array(matrix)
        res=matrix[0]
        while m!=1:
            matrix=matrix[1:]
            matrix=np.rot90(matrix, 1)
            res=np.concatenate([res, matrix[0]])
            m=len(matrix)
        
        return res
"""            
        

matrix =[[2,5],[8,4],[0,-1]]
print(Solution().spiralOrder(matrix))
