#Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#A valid BST is defined as follows:

#The left subtree of a node contains only nodes
#with keys less than the node's key.
#The right subtree of a node contains only nodes
#with keys greater than the node's key.

#Both the left and right subtrees must also be binary search trees.
import math
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
    
"""
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if root:
            stack = [[root]]
            out = [[root.val]]
        else:
            return []
        while stack:
            remember=[]
            stack_out=stack.pop()
            for i in stack_out:
                j=i.val
                if i.left:
                    if i.left.val<i.val:
                        if i.left.right:
                            if i.left.right.val<j:
                                continue
                            else: return False
                        remember.append(i.left)
                    else: return False
                if i.right:
                    if i.right.val>i.val:
                        if i.right.left:
                            if i.right.left.val>j:
                                continue
                            else: return False
                        remember.append(i.right)
                    else: return False
            if remember:
                stack.append(remember)

        return True
        """
                

root=TreeNode(6)
root.left=TreeNode(2)
root.right=TreeNode(8)
root.left.left=TreeNode(0)
root.left.right=TreeNode(4)
root.left.right.left=TreeNode(3)
root.left.right.right=TreeNode(5)
root.right.left=TreeNode(7)
root.right.right=TreeNode(9)

out=Solution().levelOrder(root)
print(out)

