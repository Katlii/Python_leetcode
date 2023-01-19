# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        """
        if not root:
            return root
        curr=root
        if curr.left is None:
            if curr.right is None:
                return root
        if curr.right:
            while curr.right:
                curr.right, curr.left=curr.left, curr.right
                curr=curr.right
        else:
            curr.left, curr.right= curr.right, curr.left
            return root
        curr=root.left
        if curr.left:
            while curr.left:
                curr.right, curr.left=curr.left, curr.right
                curr=curr.left
        return root.left.val
        """
            

root=TreeNode(1)
#root.right=TreeNode()
root.left=TreeNode(2)
#root.left.left=TreeNode(1)
#root.left.right=TreeNode(3)
#root.right.left=TreeNode(6)
#root.right.right=TreeNode(9)
out=Solution().invertTree(root)
print(out)
