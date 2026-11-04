import random

cities = [0, 1, 2, 3]
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(path):
    return sum(dist[path[i]][path[i+1]] for i in range(3)) + dist[path[-1]][path[0]]

beam = [cities]
k = 2

for _ in range(10):
    neighbors = []
    for path in beam:
        for i in range(1, 4):
            new = path[:]
            new[0], new[i] = new[i], new[0]
            neighbors.append(new)

    beam = sorted(neighbors, key=cost)[:k]

best = min(beam, key=cost)

print("Best Path:", best)
print("Minimum Distance:", cost(best))