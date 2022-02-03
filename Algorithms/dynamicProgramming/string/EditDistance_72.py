# 72. Edit Distance
# 其实这题理解也不难,因为改(替换)相当于先删再增,所以也就是在左上角,而删和增哪个在左哪个在上就没那么重要了,题解给的是增在左,删在上
# 如果相同就直接抄左上,在不在对角线上无所谓
# 如果不同就看左,上,左上三个操作的最小值加1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[i]*(len(word1)+1) for i in range(len(word2)+1)]
        dp[0] = [i for i in range(len(word1)+1)]
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[-1][-1]