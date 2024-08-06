from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}  # 记录路径

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                next_cell = (new_row, new_col)
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append(next_cell)
                    parent[next_cell] = current

    # 重建路径
    path = []
    step = end
    while step:
        path.append(step)
        step = parent.get(step)
    path.reverse()

    return path if path[-1] == end else None

n,m = input().split()
maze = []
for row in range(int(n)):
    maze.append(list(map(int,input().split())))
path = bfs(maze,(0,0),(int(n)-1,int(m)-1))
for i in path:
    print(str(i).replace(' ',''),end='\n')