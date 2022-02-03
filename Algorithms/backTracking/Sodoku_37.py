from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        task = []
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    task.append((i, j))
                    continue
                cur = int(cur) - 1
                rows[i][cur] = 1
                cols[j][cur] = 1
                boxes[i // 3][j // 3][cur] = 1

        def backTrack():
            nonlocal board
            nonlocal rows
            nonlocal cols
            nonlocal boxes
            nonlocal task
            try:
                (x, y) = task.pop(0)
            except IndexError:
                return True
            for i in range(9):
                if rows[x][i] == 1 or cols[y][i] == 1 or boxes[x // 3][y // 3][i] == 1:
                    continue
                board[x][y] = str(i + 1)
                rows[x][i] = 1
                cols[y][i] = 1
                boxes[x // 3][y // 3][i] = 1
                if backTrack() is False:
                    rows[x][i] = 0
                    cols[y][i] = 0
                    boxes[x // 3][y // 3][i] = 0
                    continue
                else:
                    return True
            task.insert(0, (x, y))
            return False

        backTrack()
        return board


if __name__ == '__main__':
    print(Solution().solveSudoku([["8", ".", ".", ".", ".", ".", ".", ".", "."],
                                  [".", ".", "3", "6", ".", ".", ".", ".", "."],
                                  [".", "7", ".", ".", "9", ".", "2", ".", "."],
                                  [".", "5", ".", ".", ".", "7", ".", ".", "."],
                                  [".", ".", ".", ".", "4", "5", "7", ".", "."],
                                  [".", ".", ".", "1", ".", ".", ".", "3", "."],
                                  [".", ".", "1", ".", ".", ".", ".", "6", "8"],
                                  [".", ".", "8", "5", ".", ".", ".", "1", "."],
                                  [".", "9", ".", ".", ".", ".", "4", ".", "."]]))
