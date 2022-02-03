class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                grid[j] += grid[j-1]
        return grid[n-1]