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

def solve_bfs(start, goal):
    queue = [(start, 0)]
    visited = {start}
    explored_count = 0
    
    while len(queue) > 0:
        current_state, depth = queue.pop(0)
        explored_count += 1
        
        if current_state == goal:
            print("BFS Result:")
            print(f"Total States Explored: {explored_count}")
            print(f"Path Cost (Depth): {depth}")
            return

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

start_node = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_node =  (0, 1, 2, 3, 4, 5, 6, 7, 8)

solve_bfs(start_node, goal_node)