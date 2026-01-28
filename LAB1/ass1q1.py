#DFS:
def dfs_all_paths(graph, current, goal, path, cost_so_far, all_paths):
    
    path.append(current)

    if current == goal:
        
        all_paths.append((list(path), cost_so_far))
    else:
     
        if current in graph:
            for neighbor, cost in graph[current]:
                
                if neighbor not in path: 
                    dfs_all_paths(
                        graph, neighbor, goal, path, 
                        cost_so_far + cost, all_paths
                    )

    
    path.pop()


# BFS
def bfs_all_paths(graph, start, goal):
  
    queue = [(start, [start], 0)]
    all_bfs_results = []

    while len(queue) > 0:
        
        current_node, path, total_cost = queue.pop(0)

        if current_node == goal:
            all_bfs_results.append((path, total_cost))
            continue 

        if current_node in graph:
            for neighbor, cost in graph[current_node]:
                if neighbor not in path:
                   
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path, total_cost + cost))
    
    return all_bfs_results


#INPUT 

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

lines = input_data.split('\n')
n, m = map(int, lines[0].split())
graph = {}

for i in range(1, m + 1):
    u, v, cost = lines[i].split()
    cost = int(cost)
    if u not in graph: graph[u] = []
    if v not in graph: graph[v] = []
    graph[u].append((v, cost))
    graph[v].append((u, cost))

start, goal = lines[m+1].split()



#Run DFS
dfs_results = []
dfs_all_paths(graph, start, goal, [], 0, dfs_results)

print(f"--- DFS: ALL PATHS FOUND ({len(dfs_results)}) ---")
for p, c in dfs_results:
    print(f"{' -> '.join(p)} | Cost = {c}")

print("\n" + "="*50 + "\n")

# Run BFS
bfs_results = bfs_all_paths(graph, start, goal)

print(f"--- BFS: ALL PATHS FOUND ({len(bfs_results)}) ---")
for p, c in bfs_results:
    print(f"{' -> '.join(p)} | Cost = {c}")

    