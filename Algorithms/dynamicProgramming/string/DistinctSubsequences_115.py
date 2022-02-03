# 115. Distinct Subsequences
# 不同时：在对角线上是0，不再对角线上跟左。因为初始值都是0，所以对角线上左边都是0，不用分开讨论
# 相同时：在对角线上时跟左上角，不同时我蒙的跟左加左上角竟然被我狗运拉满了，但是证明起来不容易
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        dp[0] = [1]*(len(s)+1)
        for i in range(len(t)):
            for j in range(i,len(s)):
                if s[j]==t[i]:
                    if i==j:
                        dp[i+1][j+1]=dp[i][j]
                        continue
                    dp[i+1][j+1] = dp[i][j]+dp[i+1][j]
                    continue
                dp[i+1][j+1] = dp[i+1][j]
        return dp[-1][-1]
if __name__=='__main__':
    # print(Solution().numDistinct("rabbbit","rabbit"))
    # print(Solution().numDistinct("rabbz", "rabz"))
    print(Solution().numDistinct("babgbag", "bag"))