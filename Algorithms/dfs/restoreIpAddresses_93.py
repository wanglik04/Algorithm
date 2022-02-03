from typing import List
'''
dfs打印所有子串，附加条件
让你找出所有可能的ip地址,字符数量和大小有要求,直接见代码
'''

class Solution:
    def dfs(self,s):
        if s=='':
            return
        if self.count==3:
            if int(s)<=255 and (s[0]!='0' or len(s)==1):
                return [[s]]
            else:
                return
        little = []
        returnlIst = []
        for i in range(3):
            self.count+=1
            i_get = self.dfs(s[i+1:])
            if i_get and int(s[:i+1])<=255 and (s[0]!='0' or len(s[:i+1])==1):
                for j in i_get:
                    little.append(s[:i+1])
                    little.extend(j)
                    returnlIst.append(little)
                    little = []
            self.count-=1
        return returnlIst





    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 13:
            return []
        self.count = 0
        self.result = []
        for i in self.dfs(s):# add .
            self.result.append('.'.join(i))
        return self.result

if __name__=='__main__':
    print(Solution().restoreIpAddresses("0000"))
    print(Solution().restoreIpAddresses("25525511135"))
    print(Solution().restoreIpAddresses("25525"))