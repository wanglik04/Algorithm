# 无向图中连通分量的数目
# dsu:只有无向图可以用dsu,也只有无向图中的环是无关紧要的,所以就算你判断再快也没乱用
class Solution:
    def __init__(self):
        self.relation_list = []

    def __str__(self):
        return str(self.relation_list)

    def find_root_r(self, node):
        if self.relation_list[node] != -1:
            self.find_root_r(self.relation_list[node])
        else:
            return node

    def find_root(self, node):
        while self.relation_list[node] != -1:
            node = self.relation_list[node]
        return node

    def connect_root(self, node1, node2):
        node1Root = self.find_root(node1)
        node2Root = self.find_root(node2)
        if node2Root == node1Root:
            print("connected")
        else:
            self.relation_list[node1Root] = node2Root

    def countComponents(self, n: int, edges: list[list]) -> int:
        self.relation_list = [(-1) for _ in range(n+1)]
        for smallList in edges:
            self.connect_root(smallList[0],smallList[1])
        return self.relation_list.count(-1)-1




if __name__ == '__main__':
    s=Solution()
    print(s.countComponents(
        5,
        [[0, 1], [1, 2], [2, 3], [3, 4]]))  #1
    print(s.countComponents(
        5,
        [[0, 1], [1, 2], [3, 4]]))  #2

    # print(s.countComponents(
    # 6,
    # [[0,1],[0,2],[2,5],[3,4],[3,5]]))  #1
