# Definition for a binary tree node.
#find the Kth smallest node in a tree
import collections
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        a=[]
        d=collections.deque()
        node=root
        d.append(node)
        a.append(node.val)
        while d:
            n=d.pop()
            if n.left:
                d.append(n.left)
                a.append(n.left.val)
            if n.right:
                d.append(n.right)
                a.append(n.right.val)
            if d:
                node=d[0]
        print(a)
        a.sort()
        for i in range(len(a)):
            if i==k-1:
                return a[i]


root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)
root.left.left=TreeNode(0)
k=1
out=Solution().kthSmallest(root, k)
print(out)
