#Given a binary search tree (BST), find the lowest common ancestor (LCA)
#node of two given nodes in the BST.

#According to the definition of LCA on Wikipedia:
#“The lowest common ancestor is defined between two nodes p and q
#as the lowest node in T that has both p and q
#as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
  
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if (p.val < root.val < q.val) or (q.val < root.val < p.val) or p == root or q == root:
            return root.val
        if p.val < root.val and q.val < root.val:
            node = self.lowestCommonAncestor(root.left, p ,q)
            return node.val
        if p.val > root.val and q.val > root.val:
            node = self.lowestCommonAncestor(root.right, p ,q)
        return node.val

root=TreeNode(6)
root.left=TreeNode(2)
root.right=TreeNode(8)
root.left.left=TreeNode(0)
root.left.right=TreeNode(4)
root.left.right.left=TreeNode(3)
root.left.right.right=TreeNode(5)
root.right.left=TreeNode(7)
root.right.right=TreeNode(9)

p=2
q=9
out=Solution().lowestCommonAncestor(root, root.left, root.right.right)
print(out)
