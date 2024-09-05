from collections import deque

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define possible moves for each position in the puzzle
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# BFS function to solve the puzzle
def bfs(initial_state):
    # Initialize the queue with the initial state and an empty path
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        # Dequeue: Pop the leftmost element from the queue
        state, path = queue.popleft()

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Find the position of '0' (empty space) in the current state
        zero_pos = state.index(0)

        # Explore all possible moves from the current position of '0'
        for move in moves[zero_pos]:
            new_state = list(state)
            # Swap '0' with the adjacent number
            new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
            new_state_tuple = tuple(new_state)

            # If the new state is not visited, enqueue it
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, path + [new_state_tuple]))

    return None


# Function to print the puzzle board
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


# Example usage:
initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
solution_path = bfs(initial_state)

if solution_path:
    print("Initial State:")
    print_board(initial_state)
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}:")
        print_board(state)
else:
    print("No solution found.")
