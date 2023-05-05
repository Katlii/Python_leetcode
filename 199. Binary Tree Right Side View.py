class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root: return root
        q = [root]
        ans = []
        while q:
            t = q.copy()
            q.clear()

            r = 0
            for node in t:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                r = node.val
            ans.append(r)
        return ans

p=TreeNode(1)
p.right=TreeNode(3)
p.left=TreeNode(2)
p.right.left=TreeNode(5)
p.left.left=TreeNode(7)
p.left.left.right=TreeNode(10)
print(Solution().rightSideView(p))
