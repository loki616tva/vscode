grid = [
    ['S', '0', '1', '0'],
    ['1', '0', '1', '0'],
    ['0', '0', '0', '0'],
    ['1', '1', '0', 'G']
]

position = [0, 0]
visited = set()

while grid[position[0]][position[1]] != 'G':
    x, y = position
    visited.add((x, y))

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if (0 <= nx < 4 and 0 <= ny < 4 and
            grid[nx][ny] != '1' and
            (nx, ny) not in visited):

            position = [nx, ny]
            break
    else:
        print("No path found!")
        break

    print("Current Position:", position)

if grid[position[0]][position[1]] == 'G':
    print("Goal Reached!")