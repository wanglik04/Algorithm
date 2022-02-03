from typing import List
'''
分割回文串
回溯，动态规划
先在字典里把所有可能的回文串放进去
剪枝的时候直接从字典中判断是否是回文串
'''
# 道理我都懂,所以为什么要管哈希表叫dp？
class Solution:
    def makeDp(self,st):
        for i in range(1, len(st) - 1):
            lin = i
            rin = i
            self.dp[st[lin:rin+1]] = 1
            while st[rin + 1] == st[rin]:
                rin += 1
                self.dp[st[lin:rin + 1]] = 1

            while st[lin - 1] == st[rin + 1]:
                lin -= 1
                rin += 1
                self.dp[st[lin:rin + 1]] = 1

    def recr(self,sr)->list[list[str]]:
        if not sr:
            return [[]]
        retls = []
        for i in range(len(sr)):
            if self.dp.get(sr[:i+1]):
                  #可以在后面加一句i+1<len
                for j in self.recr(sr[i+1:]):
                    j.insert(0,sr[:i+1])
                    retls.append(j)
        return  retls

    def partition(self, s: str) -> List[List[str]]:
        self.dp = {}
        self.makeDp('#' + s + '$')
        return self.recr(s)







if __name__=='__main__':
    # print(Solution().partition('bb'))
    print(Solution().partition('aab'))