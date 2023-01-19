# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if root:
            stack = [[root]]
            out = [[root.val]]
        else:
            return []
        while stack:
            remember=[]
            cisla=[]
            stack_out=stack.pop()
            print(stack_out)
            for i in stack_out:
                if i.left:
                    remember.append(i.left)
                    cisla.append(i.left.val)
                if i.right:
                    remember.append(i.right)
                    cisla.append(i.right.val)
            if remember:
                stack.append(remember)
            if cisla:
                out.append(cisla)
        return out
                
            


root=TreeNode(1)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
root.left.left=TreeNode(10)
root.left.right=TreeNode(6)
out=Solution().levelOrder(root)
print(out)
