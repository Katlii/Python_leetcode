# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
#Given the root of a binary tree, check whether it is
#a mirror of itself (i.e., symmetric around its center).

#Input: root = [1,2,2,3,4,4,3]
#Output: true
 

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root: return True
        stack1, stack2 = [], []
        stack1.append(root.left)
        stack2.append(root.right)
        if stack1[0] is None:
            if stack2[0]: return False
        if stack2[0] is None:
            if stack1[0]: return False
        if stack1[0] is None and stack2[0] is None: return True
        if root.right.val!=root.left.val: return False
        while stack1 and stack2 :
            node=stack1.pop()
            curr=stack2.pop()
            if node.right is not None and curr.left is not None:
                if node.right.val==curr.left.val:
                    stack1.append(node.right)
                    stack2.append(curr.left)
                else: return False
            elif node.right is None and curr.left is None:
                pass
            else: return False
            if node.left is not None and curr.right is not None:
                if node.left.val==curr.right.val:
                    stack1.append(node.left)
                    stack2.append(curr.right)
                else: return False
            elif node.left is None and curr.right is None:
                pass
            else: return False
        return True


p=TreeNode(1)
p.right=TreeNode(2)
p.left=TreeNode(2)
p.right.right=TreeNode(5)
p.left.left=TreeNode(5)

print(Solution().isSymmetric(p))
