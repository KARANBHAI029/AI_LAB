def solve_assignment():
    input_data = """14 20
Chicago Detroit 283
Chicago Cleveland 345
Chicago Indianapolis 182
Indianapolis Columbus 176
Columbus Cleveland 144
Columbus Pittsburgh 185
Cleveland Detroit 169
Cleveland Buffalo 189
Detroit Buffalo 256
Buffalo Syracuse 150
Syracuse Boston 312
Syracuse New_York 254
Boston Providence 50
Boston Portland 107
Providence New_York 181
New_York Philadelphia 97
Philadelphia Baltimore 101
Baltimore Pittsburgh 247
Pittsburgh Buffalo 215
Pittsburgh Philadelphia 305
Syracuse Chicago"""

    lines = input_data.strip().split('\n')
    target_line = lines[-1].split()
    start_node = target_line[0]
    goal_node = target_line[1]
    
    graph = {}

    for line in lines[1:-1]:
        parts = line.split()
        city1 = parts[0]
        city2 = parts[1]
        dist = int(parts[2])

        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []
        
        graph[city1].append([city2, dist])
        graph[city2].append([city1, dist])

    frontier = []
    frontier.append([0, start_node, [start_node]])
    
    reached = []
    nodes_explored_count = 0
    
    final_path = []
    final_cost = 0

    while len(frontier) > 0:
        frontier.sort()
        
        current_node_data = frontier.pop(0)
        cost = current_node_data[0]
        state = current_node_data[1]
        path = current_node_data[2]

        if state == goal_node:
            final_path = path
            final_cost = cost
            break

        if state not in reached:
            reached.append(state)
            nodes_explored_count += 1
            
            if state in graph:
                neighbors = graph[state]
                for neighbor in neighbors:
                    child_state = neighbor[0]
                    step_cost = neighbor[1]
                    
                    if child_state not in reached:
                        new_cost = cost + step_cost
                        new_path = list(path)
                        new_path.append(child_state)
                        frontier.append([new_cost, child_state, new_path])

    print("Best First Search ")
    print("Start:", start_node)
    print("Goal:", goal_node)
    print("Path found:", final_path)
    print("Total Cost:", final_cost)
    print("Total nodes explored:", nodes_explored_count)

solve_assignment()