from collections import defaultdict, OrderedDict
from typing import List
# 细节还是挺多的就不多讲了,简单说就是有向图dfs,通过每次要学那门课程就把那门课程在字典中pop出来,以此来鉴定如果pop报KeyError了就说明有重复访问同一门课程,也就是说存在环

class Solution:
    def dfs(self,cur):
        try: # 如果不存在说明有环(重复访问同一个节点)
            need_list = self.requirement.pop(cur)
        except KeyError:
            self.isValid = False
            return
        if need_list==[]: # 所谓的入度为零
            self.has_learned[cur] = 1
            return
        for need in need_list:
            if not self.has_learned.get(need):
                self.dfs(need)
                self.has_learned[need] = 1
        self.has_learned[cur] = 1

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.isValid = True
        self.numCoursesLeft = []
        self.requirement = {}  # 不能用defaultdict因为必须保证每个课程都要出现,不然会和上面的try冲突
        for i in range(numCourses):
            self.numCoursesLeft.append(i)
            self.requirement[i] = []
        while prerequisites:
            i = prerequisites.pop()
            self.requirement[i[0]].append(i[1])
        self.result = []
        self.has_learned = OrderedDict()  # 通过学习顺序直接出结果
        for i in range(numCourses):
            if not self.has_learned.get(i):
                self.dfs(i)
        return [i for i in self.has_learned] if self.isValid==True else []
if __name__=='__main__':
    # print(Solution().findOrder(1,[]))
    print(Solution().findOrder(3, [[1,0],[2,0]]))
    print(Solution().findOrder(3, [[1, 0]]))
    print(Solution().findOrder(2, [[0, 1], [1, 0]]))