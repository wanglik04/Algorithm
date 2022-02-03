import copy


class Solution:
    def solver(self,l:list,m:list,r:list):
        self.cur += 1
        g = [i for i in range(self.finish) if i not in l and i not in m and i not in r]
        if g==[]:
            return
        if self.cur == self.finish-1:
            for j in g:
                self.smallResult.append(j)
                self.result.append(copy.deepcopy(self.smallResult))
                self.smallResult.pop()
            return
        l = [j-1 for j in l if j-1>=0]
        r = [j+1 for j in r if j+1<self.finish]
        for smindx in g:
            smallL,smallM,smallR = copy.deepcopy(l),copy.deepcopy(m),copy.deepcopy(r)  # 也算回溯
            self.smallResult.append(smindx)
            smallM.append(smindx)
            if smindx - 1 >= 0:
                smallL.append(smindx - 1)
            if smindx + 1 < self.finish:
                smallR.append(smindx + 1)
            self.solver(smallL, smallM, smallR)
            self.smallResult.pop()  # 回溯体现
            self.cur-=1  # 太多回溯啦！

    def solveNQueens(self, n: int):
        self.smallResult = []
        self.finish = n
        self.cur = -1  # cur layer
        self.result = []
        l,m,r = [],[],[]
        self.solver(l,m,r)
        # return len(self.result)
        realAns = []
        for i in self.result:
            ans = []
            for j in i:
                a = ['.'] * n
                a[j] = 'Q'
                ans.append(''.join(a))
            realAns.append(ans)
        return realAns


if __name__=='__main__':
    # for i in range(10):
    #
    print(Solution().solveNQueens(7))


    # class Solution:
    #     def totalNQueens(self, n: int) -> int:
    #         return {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}.get(n)













