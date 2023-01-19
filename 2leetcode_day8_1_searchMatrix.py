#You are given an m x n integer matrix matrix with the following two properties:

#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix[0])
        middle=m//2
        n=len(matrix)
        logic=False
        i,j=0,0
        while logic==False:
            if target> matrix[i][j]:
                if target<matrix[i][m-1]:
                   if target>matrix[i][middle]:
                       j=middle+1
                       middle=(middle+m-1)//2
                   elif target==matrix[i][middle]:
                       logic=True
                       return True
                   else:
                        if target>matrix[i][middle-1]:
                            logic=False
                            return logic

                        else:
                            j=middle-1
                            middle=middle//2

                elif target==matrix[i][m-1]:
                    logic=True
                    return logic

                else:
                    i+=1
                    if i==n:
                        logic=False
                        return False
                    

            elif target==matrix[i][j]:
                logic=True
                return True
            else:
                return False
            
                    
matrix=[[1,3,5,7, 9],[10,11,16,20, 21],[23,30,34,60, 65], [70, 100, 120, 140, 150]]
target=16
out=Solution().searchMatrix(matrix, target)
print(out)
