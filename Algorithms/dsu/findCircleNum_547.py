from typing import List


class Solution:
    def connect(self,i,j):
        while self.dsu[i] != -1:
            i = self.dsu[i]
        while self.dsu[j] != -1:
            j = self.dsu[j]
        if i==j:
            return
        self.dsu[i] = j
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        self.dsu = [-1]*length
        improve = 1
        for i in range(length):
            for j in range(improve,length):
                if isConnected[i][j]==1:
                    self.connect(i,j)
                else:
                    continue
            else:
                improve+=1
        return self.dsu.count(-1)
if __name__=='__main__':
    print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))