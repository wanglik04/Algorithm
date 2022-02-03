'''
让你把所有叶子结点的next指向右边
用了经典的层序遍历，然后如果右边为空就指向None
题目让你将所有左子树的next指向右子树
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: [Node]) -> [Node]:
        if root==None:
            return root
        q = [root]
        next_level = []
        while q:
            while q:
                cur = q.pop(0)
                try:
                    cur.next = q[0]
                except IndexError:
                    cur.next = None
                if cur.left:
                    next_level.append(cur.left)
                    next_level.append(cur.right)
            q = next_level
            next_level = []
        return root