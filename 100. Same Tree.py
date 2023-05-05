#Given the roots of two binary trees p and q,
#write a function to check if they are the same or not.

#Input: p = [1,2], q = [1,null,2]
#Output: false


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q: return True
        if not p:
            if q: return False
        if not q:
            if p: return False    
        tree1, tree2 =[p], [q]
        if p.val!=q.val: return False
        while tree1 and tree2 :
            node=tree1.pop()
            curr=tree2.pop()
            if node.right is not None and curr.right is not None:
                if node.right.val==curr.right.val:
                    tree1.append(node.right)
                    tree2.append(curr.right)
                else: return False
            elif node.right is None and curr.right is None:
                pass
            else: return False
            if node.left is not None and curr.left is not None:
                if node.left.val==curr.left.val:
                    tree1.append(node.left)
                    tree2.append(curr.left)
                else: return False
            elif node.left is None and curr.left is None:
                pass
            else: return False
        return True
                
            
            
p=TreeNode(1)
#p.right=TreeNode(2)
p.left=TreeNode(-5)

q=TreeNode(1)
#q.right=TreeNode(2)
q.left=TreeNode(-8)

print(Solution().isSameTree(p, q))
