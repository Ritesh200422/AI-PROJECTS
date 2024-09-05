from collections import deque

# Define the maximum capacities of the jugs
jug1_capacity = 4  # Capacity of jug 1 (in liters)
jug2_capacity = 3  # Capacity of jug 2 (in liters)

# Define the goal amount of water to be measured
goal_amount = 2  # The target amount of water (in liters)


# Function to perform BFS to find the solution
def bfs_water_jug_problem():
    queue = deque([(0, 0, 0)])  # (jug1_current, jug2_current, steps)
    visited = set()  # To keep track of visited states

    while queue:
        jug1_current, jug2_current, steps = queue.popleft()

        # Check if the current state is the goal state
        if jug1_current == goal_amount or jug2_current == goal_amount:
            print(f"Goal reached in {steps} steps.")
            return

        # Generate all possible next states from the current state
        next_states = [
            (jug1_capacity, jug2_current),  # Fill jug 1 to its capacity
            (jug1_current, jug2_capacity),  # Fill jug 2 to its capacity
            (0, jug2_current),  # Empty jug 1
            (jug1_current, 0),  # Empty jug 2
            (jug1_current - min(jug1_current, jug2_capacity - jug2_current),
             jug2_current + min(jug1_current, jug2_capacity - jug2_current)),  # Pour from jug 1 to jug 2
            (jug1_current + min(jug2_current, jug1_capacity - jug1_current),
             jug2_current - min(jug2_current, jug1_capacity - jug1_current))  # Pour from jug 2 to jug 1
        ]

        # Iterate over each next state and add to the queue if not visited
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((*state, steps + 1))

    print("No solution found.")


# Solve the water jug problem using BFS
bfs_water_jug_problem()
