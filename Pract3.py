from queue import PriorityQueue

goal = ((1,2,3), (4,5,6), (7,8,0))

def heuristic(state):
    # Calculate the Manhattan distance of all numbered tiles.
    d = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x, y = (value-1)//3, (value-1)%3
                d += abs(i-x) + abs(j-y)
    return d

def get_neighbors(state):
    # Store all valid next states here.
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [list(row) for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            # Convert the grid into an immutable tuple.
            neighbors.append(tuple(tuple(row) for row in temp))
    return neighbors

def print_matrix(state):
    for row in state:
        print(row, end="")
        print()

def astar(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start, [start]))
    visited = set()

    while not pq.empty():
        f, g, state, path = pq.get()

        if state == goal:
            print("Goal Reached!")
            print("Total Steps:", g)
            print("Total Matrices:", len(path))
            for i, matrix in enumerate(path):
                print("Step", i+1, ":")
                print_matrix(matrix)
            return

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

    print("No Solution")

start = ((1,2,3), (4,0,6), (7,5,8))
astar(start)
