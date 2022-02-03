# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         self.isOK = True
#         self.validate(root,  -2147483649, 2147483649)
#         return self.isOK
#
#     def validate(self, t, L, H):  #t为结点，L为最低值，H为最高值
#         if self.isOK:
#             if t.val >= H or t.val <= L:
#                 self.isOK = False
#             if t.left != None:
#                 self.validate(t.left, L, t.val)
#             if t.right != None:
#                 self.validate(t.right, t.val, H)
# Definition for a binary tree node.
# 判断一个二叉搜索树是否合法.中心思想就是利用二叉搜索树在任何情况下都严格遵守:左儿子<父节点<右节点的特点
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node,up,down):
            if node is None:
                return True
            if up>node.val>down and check(node.left,node.val,down) and check(node.right,up,node.val):
                return True
            return False
        return check(root,-999,1000)

if __name__=='__main__':
    A, B, C, D, E = TreeNode(5),TreeNode(4),TreeNode(6),TreeNode(3),TreeNode(7)
    A.left = B
    A.right = C
    # C.left = D
    C.right = E
    print(Solution().isValidBST(A))