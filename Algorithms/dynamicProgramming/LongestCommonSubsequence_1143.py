# 1143. Longest Common Subsequence
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i]==text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    continue
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]


if __name__=='__main__':
    ...