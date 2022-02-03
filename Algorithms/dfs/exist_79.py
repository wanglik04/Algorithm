from typing import List
# 这题典型的dfs.就是从头到尾把列表遍历一遍,一旦发现有和当前字符串首字母相同的,就把当前坐标做个标记,避免重复使用,然后把当前坐标和去首字符串传到下一层递归。,

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        around = [(1,0),(0,1),(-1,0),(0,-1)]
        row = len(board)
        col = len(board[0])
        mark = [[0]*col for _ in range(row)]
        ##
        def check(x,y,tar):
            if tar=='':
                return True
            for i in around:
                newX = i[0]+x
                newY = i[1]+y
                if row > newX > -1 and -1 < newY < col and board[newX][newY]==tar[0]:
                    if mark[newX][newY] == 1:
                        continue
                    mark[newX][newY] = 1
                    if check(newX,newY,tar[1:]):
                        return True
                    else:
                        mark[newX][newY] = 0

        ##

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if check(i,j,word[1:]):
                        return True
                    else:
                        mark[i][j] = 0
        return False

if __name__=='__main__':
    # board = [["A", "B", "C", "E"],
    #          ["S", "F", "C", "S"],
    #          ["A", "D", "E", "E"]]
    # word = "ABCCED"
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCB"
    board = [["C", "A", "A"],
             ["A", "A", "A"],
             ["B", "C", "D"]]
    word = "AAB"
    print(Solution().exist(board,word))