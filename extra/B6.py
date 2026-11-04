blocks = {'A': 'Table', 'B': 'A', 'C': 'Table'}
goal = {'A': 'B', 'B': 'Table', 'C': 'A'}

def move(block, dest):
    blocks[block] = dest
    print("Move", block, "to", dest)

for block in goal:
    if blocks[block] != goal[block]:
        move(block, goal[block])

print("Goal State:", blocks)