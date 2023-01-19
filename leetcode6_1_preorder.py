
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root) -> list[int]:
        res = []
        stack = [root]
        
        while len(stack)!=0:
            x = stack.pop()
            if x:
                res.append(x.val)
                for c in reversed(x.children):
                    stack.append(c)
        return res


root=Node(1)
root.children=Node(3)
root.children.children=Node(2)
root.children.children.children=Node(4)
root.children.children.children.children=Node(5)
root.children.children.children.children.children=Node(6)
out=Solution().preorder(root)
print(out)
