from collections import deque

grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

q = deque([(start, [start])])
visited = {start}

while q:
    (x, y), path = q.popleft()

    if (x, y) == goal:
        print("Path:", path)
        break

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        pos = (nx, ny)

        if (0 <= nx < 4 and 0 <= ny < 4 and
            grid[nx][ny] == 0 and pos not in visited):

            visited.add(pos)
            q.append((pos, path + [pos]))
else:
    print("No path found")