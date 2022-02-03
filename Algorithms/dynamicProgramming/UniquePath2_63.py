from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        for col in range(len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                for i in range(col,len(obstacleGrid[0])):
                    obstacleGrid[0][i] = 0
                break
            else:
                obstacleGrid[0][col] = 1
        for row in range(1,len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                for i in range(row,len(obstacleGrid)):
                    obstacleGrid[i][0] = 0
                break
            else:
                obstacleGrid[row][0] = 1
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0


        return obstacleGrid[-1][-1]