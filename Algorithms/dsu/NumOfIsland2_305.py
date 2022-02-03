class Solution:
    def __init__(self):
        self.relation_dict = {}
        self.ansList = []

    """
    先在字典里创建。
    判断四周有没有相邻，有的话链接，没有的话下一个
    """
    # def returnFist(self,l:list):
    #     return l[0]
    # def returnSecond(self,l:list):
    #     return l[1]

    def look_around_and_connect(self, core_point: tuple):
        """
        返回不同根的tuple
        :param core_point:
        :return:
        """
        count = -1
        left_node, right_node, up_node, down_node = (core_point[0], core_point[1] - 1), (core_point[0], core_point[1] + 1), (core_point[0] - 1, core_point[1]), (core_point[0] + 1, core_point[1])
        if left_node in self.relation_dict and self.connect_root(left_node,core_point):
            count+=1
            # return (core_point[0], core_point[1] - 1)
        if right_node in self.relation_dict and self.connect_root(right_node,core_point):
            count += 1
            # return (core_point[0] - 1, core_point[1])
        if up_node in self.relation_dict and self.connect_root(up_node,core_point):
            count += 1
            # return (core_point[0], core_point[1] + 1)
        if down_node in self.relation_dict and self.connect_root(down_node,core_point):
            count += 1
            # return (core_point[0] + 1, core_point[1])
        return count

    def __find_root(self, node):
        """
        for connection
        :param node:
        :return:
        """
        while self.relation_dict[tuple(node)] != -1:
            node = self.relation_dict[node]
        return node

    def connect_root(self, node1, node2):
        node1, node2 = self.__find_root(node1), self.__find_root(node2)
        if node1 != node2:
            self.relation_dict[node1] = node2
            return True

    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        # positions.sort(key=self.returnSecond)
        # positions.sort(key=self.returnFist)
        while positions:
            small_position = tuple(positions.pop(0))
            if small_position not in self.relation_dict:
                self.relation_dict[small_position] = -1
                findAnything = self.look_around_and_connect(small_position)
                if findAnything != -1:
                    self.ansList.append(self.ansList[-1]-findAnything)
                else:
                    if not self.ansList:
                        self.ansList.append(1)
                    else:
                        self.ansList.append(self.ansList[-1]+1)
            else:
                self.ansList.append(self.ansList[-1])

        return self.ansList


if __name__ == '__main__':
    print(Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))#1123
    print(Solution().numIslands2(1, 1, [[0, 0]]))  # 1
    print(Solution().numIslands2(2, 2,
[[0,0],[1,1],[0,1]]))  # 121
    print(Solution().numIslands2(2, 2,
    [[0, 0], [0, 1], [1, 2], [1, 2]]))#1122
