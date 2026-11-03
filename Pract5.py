from collections import deque

# Initial and goal states of Tower of Hanoi
start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

def bfs():
    # Queue stores the current state and its movement path
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        # Remove the first state from the queue (FIFO)
        state, path = queue.popleft()

        # Check whether the goal state is reached
        if state == goal:
            for move in path:
                print(move)
            print("Total moves:", len(path))
            return

        # Select each tower as the source tower
        for i in range(3):
            if state[i]:
                disk = state[i][-1]  # Get the top disk

                # Check all towers as possible destination towers
                for j in range(3):

                    # Move only if destination is different and follows disk-size rules
                    if i != j and (not state[j] or state[j][-1] > disk):

                        # Create a temporary copy of the towers
                        towers = [list(t) for t in state]

                        towers[i].pop()          
                        towers[j].append(disk)   

                        # Convert the new state into tuples
                        new_state = tuple(tuple(t) for t in towers)

                        # Avoid visiting the same state again
                        if new_state not in visited:
                            visited.add(new_state)

                            # Add the new state and updated path to the queue
                            queue.append((new_state, path + [
                                ("Disk", disk, "from", chr(65+i),
                                 "to", chr(65+j))]))

bfs()















