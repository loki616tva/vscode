
def water_jug_dfs(a, b, target):
    visited = set()  # Stores already visited states to avoid repetition

    def dfs(x, y, path):
        if (x, y) in visited:
            return None

        visited.add((x, y))
        path = path + [(x, y)]  # Add current state to the solution path

        if x == target or y == target:  # Check if target amount is reached
            return path

        # Generate all possible next states (fill, empty, and pour operations)
        states = [
            (a, y), (x, b), (0, y), (x, 0),
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        # Explore each possible state using DFS
        for nx, ny in states:
            result = dfs(nx, ny, path)
            if result:
                return result  # Return the solution path if found

        return None  # No solution found from this state

    return dfs(0, 0, [])  # Start with both jugs empty


print(water_jug_dfs(4, 3, 2))  # Jug capacities: 4L and 3L, target: 2L