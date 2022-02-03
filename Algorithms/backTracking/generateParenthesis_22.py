# 我一直觉得只要不改变当前值,直接将变化的量输入到下一层递归中去就可以实现没有回溯操作但有回溯思想的函数
from typing import List
# 这题用了回溯剪枝思想,详情见图

class Solution:
    def backtracking(self,s:str):
        if self.check(s) is False:
            return
        for i in self.for_list:
            self.backtracking(s+i)
    def check(self,s:str):
        # 如果是合法且完整的话也返回false只不过多加一个添加操作
        left = self.length - len(s)
        count = 0
        for i in s:
            if i=='(':
                count+=1
            else:
                count-=1
        if count==0:
            if left==0:
                self.result.append(s)
                return False
            return True
        if count<0:
            return False
        if left<count:
            return False
        return True
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.length = n*2
        self.for_list = ['(',')']
        self.backtracking('(')
        return self.result