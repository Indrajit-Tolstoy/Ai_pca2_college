import heapq

def manhattan_distance(state, target):
    """Calculates the Manhattan distance heuristic for A* search."""
    distance = 0
    for i, val in enumerate(state):
        if val != 0:
            target_idx = target.index(val)
            # Convert 1D index into 2D (row, col) coordinates to find distance
            curr_row, curr_col = divmod(i, 3)
            target_row, target_col = divmod(target_idx, 3)
            distance += abs(curr_row - target_row) + abs(curr_col - target_col)
    return distance

def solve_8_puzzle(start_state):
    target_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    # Pre-calculated valid swap indices for a 1D representation of a 3x3 grid
    # e.g., if '0' is at index 0 (top-left), it can only swap with index 1 or 3
    moves = {
        0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
        3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
        6: (3, 7), 7: (4, 6, 8), 8: (5, 7)
    }

    # Priority Queue stores tuples of: (priority_score, path_cost, current_state, path_taken)
    pq = [(0, 0, start_state, [])]
    visited = set()

    while pq:
        _, cost, state, path = heapq.heappop(pq)

        if state == target_state:
            return path + [state] # Solution found!

        if state in visited:
            continue
        visited.add(state)

        zero_idx = state.index(0)
        
        # Generate all possible next states
        for swap_idx in moves[zero_idx]:
            # Convert tuple to list to swap, then back to tuple
            new_board = list(state)
            new_board[zero_idx], new_board[swap_idx] = new_board[swap_idx], new_board[zero_idx]
            new_state = tuple(new_board)

            if new_state not in visited:
                new_cost = cost + 1
                # f(n) = g(n) + h(n)  --> Total Cost = Path Cost + Heuristic Guess
                priority = new_cost + manhattan_distance(new_state, target_state)
                heapq.heappush(pq, (priority, new_cost, new_state, path + [state]))

    return "No solution possible"

# --- Testing the Code ---
if __name__ == "__main__":
    # 0 represents the empty space
    start = (1, 2, 3, 4, 0, 5, 7, 8, 6) 
    
    print("Solving 8-Puzzle...")
    solution_path = solve_8_puzzle(start)
    
    if type(solution_path) == str:
        print(solution_path)
    else:
        print(f"Solved in {len(solution_path) - 1} moves!")
        for step, board in enumerate(solution_path):
            print(f"Step {step}:")
            print(f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}\n")