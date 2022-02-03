import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        参数定义
        l/r：左右子树高度
        depth：当前节点离叶子节点高度
        res：哈希表，记录每个深度对应的节点值集合
        思路
        根据题意，一层层将叶子节点删除，叶子节点被删除后其父节点会变为叶子节点，所以我们需要自底向上递归来记录每个节点离叶子节点的高度，将不同深度的节点放入对应的集合即可。
        心得：善于发现题目规律，学会融会贯通，才能触类旁通

        作者：yim-6
        链接：https://leetcode-cn.com/problems/find-leaves-of-binary-tree/solution/python3-zi-di-xiang-shang-di-gui-qiu-she-ma41/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param root:
        :return:
        """
        # 自底向上递归
        def dfs(root):
            if not root:return 0
            l,r=dfs(root.left),dfs(root.right)
            depth=max(l,r)+1
            res[depth].append(root.val)
            return depth

        res=collections.defaultdict(list)
        dfs(root)
        return [v for v in res.values()]



def listCreatTree(root, Node_list, i):
    """
    Nodelist = [1, 2, 3, 4, 5]
    Nodelist_strItem = [str(i) for i in Nodelist]
    levelOrder(listCreatTree(None, Nodelist_strItem, 0))
    :param root:
    :param Node_list:
    :param i:
    :return:
    """
    if i < len(Node_list):
        if Node_list[i] == '#':
            return None  # 这里的return很重要
        else:
            root = TreeNode(Node_list[i])
            # 往左递推
            root.left = listCreatTree(root.left, Node_list, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, Node_list, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  # 这里的return很重要
    return root
if __name__=='__main__':
    print(Solution().findLeaves(listCreatTree(None,[1, 2, 3, 4, 5],0)))
