# class Solution:
#     def numSquares(self, n: int) -> int:
#         stateCompress = [i for i in range(n+1)]
#         maxSquare = int(pow(n, 0.5))
#         squareList = [i ** 2 for i in range(2,maxSquare+1)]
#         for j in squareList:
#             for i in range(j,len(stateCompress)): # 从j开始很重要因为当i<j时也是不变,i==j时在数列前面加个0也不用判断了
#                 stateCompress[i] = min(stateCompress[i], stateCompress[i - j] + 1)
#         return stateCompress[-1]

# 这道题用bfs很快,用当前值不断减去小正方形
class Solution:
    def numSquares(self, n: int) -> int:
        q = [n]
        cnt = 1
        while q:
            nextq = set()  # set()?
            for tar in q:
                for squareRoot in range(1,tar+1):
                    square = squareRoot*squareRoot
                    if square==tar:
                        return cnt
                    if tar>square:
                        nextq.add(tar-square)
                    else:
                        break
                    # nextq.add(tar-square) if tar>square else break
            q = list(nextq)
            cnt += 1

if __name__=='__main__':
    print(Solution().numSquares(1))
