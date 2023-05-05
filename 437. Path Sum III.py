#Given the root of a binary tree and an integer targetSum,
#return the number of paths where the sum of the values along
#the path equals targetSum.

#The path does not need to start or end at the root or a leaf,
#but it must go downwards (i.e., traveling only from parent nodes to child nodes).

                                  #Example
#Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
#Output: 3

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
     def pathSum(self, root, target: int) -> int: 
        # define global result and path
        self.result=0
        cache={0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
     def dfs(self, root, target, currPathSum, cache):
         # exit condition
        if root is None: return 
        # calculate currPathSum and required oldPathSum
        currPathSum+=root.val
        oldPathSum=currPathSum-target
        # update result and cache
        self.result+=cache.get(oldPathSum, 0)
        cache[currPathSum]=cache.get(currPathSum, 0)+1
        # dfs recurse
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum]-=1
     
            


node=TreeNode(1)
node.left=TreeNode(3)
node.right=TreeNode(5)
node.left.left=TreeNode(1)
node.left.right=TreeNode(-2)
node.left.left.left=TreeNode(5)
node.left.left.right=TreeNode(0)
node.left.right.right=TreeNode(1)
node.right.right=TreeNode(0)
node.right.left=TreeNode(5)

target=5
print(Solution().pathSum(node, target))


