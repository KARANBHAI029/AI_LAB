def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = idx // 3, idx % 3
    moves = [(-1, 0, -3), (1, 0, 3), (0, -1, -1), (0, 1, 1)]

    for r_move, c_move, idx_move in moves:
        new_row, new_col = row + r_move, col + c_move
        if 0 <= new_row <= 2 and 0 <= new_col <= 2:
            temp = list(state)
            temp[idx], temp[idx + idx_move] = temp[idx + idx_move], temp[idx]
            neighbors.append(tuple(temp))
    return neighbors

def solve_dfs(start, goal):
    stack = [(start, 0)]
    visited = {start}
    explored_count = 0
    limit = 200000 
    
    while len(stack) > 0:
        current_state, depth = stack.pop()
        explored_count += 1
        
        if current_state == goal:
            print("DFS Result:")
            print(f"Total States Explored: {explored_count}")
            print(f"Path Cost (Depth): {depth}")
            return

        if explored_count >= limit:
            print("DFS Result:")
            print(f"Stopped at limit: {limit}")
            return

        neighbors = get_neighbors(current_state)
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, depth + 1))

start_node = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_node =  (0, 1, 2, 3, 4, 5, 6, 7, 8)

solve_dfs(start_node, goal_node)


#start state
#(3 ,1 , 2, 6 , 4 , 5, 0 , 7 , 8)

#goal state
#(0 , 1 , 2, 3  ,4  ,5 , 6,  7 , 8)