#当前节点的最大smaller value等于左移一格的最右
#当前节点的最小bigger value等于右移一格的最左
# 题目让你在一棵二叉搜索树中,找到并返回大于且仅次于当前节点的值
# 因为是一个二叉搜索树,所以如果当前节点有右儿子那最好了.直接返回右儿子的最小值(也就是最左边的根)
# 如果不巧右子树为空,那就从头开始找,公式见前两行
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def dfs(self,node:TreeNode):
        if node==self.p:
            self.valid = True
            return
        if node.val<self.p.val:
            self.dfs(node.right)
        elif node.val>self.p.val:
            self.result = node
            self.dfs(node.left)
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        else:
            self.valid = False
            self.result = None
            self.p = p
            self.dfs(root)
            return self.result if self.valid==True else None