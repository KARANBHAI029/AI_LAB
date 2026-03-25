def solve_robot_evacuation():
    # Row 0: Room Wall Room Room -> ####
    # Row 1: Wall Space Space Exit -> #..E
    # Row 2: Wall Entry Room Room -> #S##
    floor_plan = [
        "####",
        "#..E",
        "#S##"
    ]

    graph = {}
    rows = len(floor_plan)
    cols = len(floor_plan[0])
    
    start_node = None
    goal_node = None

    def get_id(r, c):
        return str(r) + "," + str(c)

    for r in range(rows):
        for c in range(cols):
            char = floor_plan[r][c]
            
            current_id = get_id(r, c)
            if char == 'S':
                start_node = current_id
            elif char == 'E':
                goal_node = current_id
            
            if char != '#':
                if current_id not in graph:
                    graph[current_id] = []
                
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        neighbor_char = floor_plan[nr][nc]
                        if neighbor_char != '#':
                            neighbor_id = get_id(nr, nc)
                            graph[current_id].append([neighbor_id, 1])

    print("Best First Search (")
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)
    
    frontier = []
    frontier.append([0, start_node, [start_node]])
    
    reached = []
    nodes_explored = 0
    
    final_path = []
    final_cost = 0
    found = False

    while len(frontier) > 0:
        frontier.sort()
        
        current_data = frontier.pop(0)
        cost = current_data[0]
        node = current_data[1]
        path = current_data[2]
        
        if node == goal_node:
            final_path = path
            final_cost = cost
            found = True
            break
        
        if node not in reached:
            reached.append(node)
            nodes_explored += 1
            
            if node in graph:
                neighbors = graph[node]
                for neighbor in neighbors:
                    child_node = neighbor[0]
                    step_cost = neighbor[1]
                    
                    if child_node not in reached:
                        new_cost = cost + step_cost
                        new_path = list(path)
                        new_path.append(child_node)
                        frontier.append([new_cost, child_node, new_path])

    if found:
        print("Route Found!")
        print("Cost:", final_cost)
        print("Nodes Explored:", nodes_explored)
        print("Path:", final_path)
        
        print("\n--- GRID MAP ---")
        for r in range(rows):
            line_str = ""
            for c in range(cols):
                node_id = get_id(r, c)
                if node_id in final_path:
                    if floor_plan[r][c] == 'S':
                        line_str += "S "
                    elif floor_plan[r][c] == 'E':
                        line_str += "E "
                    else:
                        line_str += "* "
                else:
                    val = floor_plan[r][c]
                    if val == '#':
                         line_str += "# "
                    else:
                         line_str += ". "
            print(line_str)
    else:
        print("No route found.")

solve_robot_evacuation()