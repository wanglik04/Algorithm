from typing import List

'''
寻找名人
深度优先搜索，改来改去真的没意思，每次要判断只有当所有人都认识他且他不认识所有人时才能添加
'''
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    graph = [[1,0],[0,1]]
    return True if graph[a][b] == 1 else False


class Solution:
    def find(self,i):
        for j in range(self.n):
            if knows(i,j) and j!=i:
                if self.name_list[j]==0:
                    self.name_list[j]=1
                    self.find(j)
                return
            elif not knows(j,i):
                return
        self.result = i
        return
    def findCelebrity(self, n: int) -> int:
        self.n = n
        self.result = -1
        self.name_list = {i:0 for i in range(n)}
        for i in range(n):
            if self.name_list[i]==0 and self.result==-1:
                self.name_list[i]=1
                self.find(i)
        return self.result


if __name__=='__main__':
    # print(Solution().findOrder(2,[[1,0]]))
    # print(Solution().findOrder(1,[]))
    # print(Solution().findOrder(3, [[1,0],[2,0]]))
    # print(Solution().findOrder(3, [[1, 0]]))
    # print(Solution().findOrder(2, [[0, 1], [1, 0]]))
    print(Solution().findCelebrity(2))