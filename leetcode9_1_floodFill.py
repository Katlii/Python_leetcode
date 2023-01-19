class Solution:
    def floodFill(self, image: list[list[int]], i: int, j: int, color: int) -> list[list[int]]:
        if image[i][j]==color: return image
        N=len(image)-1
        n=len(image[0])-1
        stack=[[i,j]]
        s=set()
        s.add((i,j))
        a=image[i][j]
        image[i][j]=color
        while stack!=[]:
            b=stack.pop()
            i=b[0]
            j=b[1]
            i-=1
            if i>=0 and i<=N:
                if (i,j) not in s and  image[i][j]==a:
                    stack.append([i,j])
                    s.add((i,j))
                    image[i][j]=color
            i+=2
            if i>=0 and i<=N:
                if (i,j) not in s and image[i][j]==a:
                    stack.append([i,j])
                    s.add((i,j))
                    image[i][j]=color
            i-=1
            j+=1
            if j>=0 and j<=n:
                if (i,j) not in s and image[i][j]==a:
                    stack.append([i,j])
                    s.add((i,j))
                    image[i][j]=color
            j-=2
            if j>=0 and j<=n:
                if (i,j) not in s and image[i][j]==a:
                        stack.append([i,j])
                        s.add((i,j))
                        image[i][j]=color
            j+=1
        return image
        


image = [[1,1,0,1],[0,1,0,1], [1,1,0,1], [0,0,1,1]]
sr = 1
sc = 1
color = 2
out=Solution().floodFill(image, sr, sc, color)
print(out)



        
