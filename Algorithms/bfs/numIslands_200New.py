"""
0。初始化队列
1。将当前点变成0,入队
2。寻找当前点周围的1，并将结果存入队列
3。将找到的1都变成0
4。取出队列的一个值，goto步骤1，直至队列结束，循环结束
"""
#仔细想想也算是bfs的一种把

def fillWater(grid, c, line):
    queue = []
    grid[line][c] = "0"
    queue.append([line, c])
    while queue:
        queue = clearAround(grid, queue)


def clearAround(grid, Newqueue):
    [line, c] = Newqueue.pop(0)

    # right
    if c + 1 < len(grid[0]) and grid[line][c + 1] == "1":
        grid[line][c + 1] = "0"
        Newqueue.append([line, c + 1])
    # left
    if 0 <= c - 1 and grid[line][c - 1] == "1":
        grid[line][c - 1] = "0"
        Newqueue.append([line, c - 1])

    # up
    if line - 1 >= 0 and grid[line - 1][c] == "1":
        grid[line - 1][c] = "0"
        Newqueue.append([line - 1, c])

    # down
    if line + 1 < len(grid) and grid[line + 1][c] == "1":
        grid[line + 1][c] = "0"
        Newqueue.append([line + 1, c])
    return Newqueue


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for line in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[line][c] == "1":
                fillWater(grid, c, line)
                count += 1
    return count


# grid=[["1","1","1"],
#       ["0","1","0"],
#       ["1","1","1"]]
# grid=[["1","1","1"],
#       ["0","1","0"],
#       ["0","1","0"]]
# grid=[["1","1","1"],
#       ["1","0","1"],
#       ["1","1","1"]]
# grid=[["1","1","0","0","0"],
#       ["1","1","0","0","0"],
#       ["0","0","1","0","0"],
#       ["0","0","0","1","1"]]
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid))
