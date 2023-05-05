#Given the root of a binary search tree, and an integer k,
#return the kth smallest value (1-indexed) of all the values
#of the nodes in the tree.

                        #Example
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3

import collections
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack=[root]
        res=[root.val]
        while stack:
             node=stack.pop()
             if node.right is not None:
                  stack.append(node.right)
                  res.append(node.right.val)
             if node.left is not None:
                  stack.append(node.left)
                  res.append(node.left.val)
        res.sort()
        return res[k-1]




node=TreeNode(5)
node.left=TreeNode(3)
node.right=TreeNode(6)
node.left.left=TreeNode(2)
node.left.right=TreeNode(4)
node.left.left.left=TreeNode(1)
k=3
print(Solution().kthSmallest(node, k))
