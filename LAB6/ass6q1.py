# Graph and Heuristics based on your data
graph = {
    'Chicago': [('Detroit', 283), ('Cleveland', 345), ('Indianapolis', 182)],
    'Indianapolis': [('Chicago', 182), ('Columbus', 176)],
    'Columbus': [('Indianapolis', 176), ('Cleveland', 144), ('Pittsburgh', 185)],
    'Cleveland': [('Chicago', 345), ('Detroit', 169), ('Columbus', 144), ('Buffalo', 189)],
    'Detroit': [('Chicago', 283), ('Cleveland', 169), ('Buffalo', 256)],
    'Buffalo': [('Cleveland', 189), ('Detroit', 256), ('Syracuse', 150), ('Pittsburgh', 215)],
    'Pittsburgh': [('Columbus', 185), ('Buffalo', 215), ('Philadelphia', 305), ('Baltimore', 247)],
    'Syracuse': [('Buffalo', 150), ('Boston', 312), ('New_York', 254)],
    'Boston': [('Syracuse', 312), ('Providence', 50), ('Portland', 107)],
    'Providence': [('Boston', 50), ('New_York', 181)],
    'New_York': [('Syracuse', 254), ('Providence', 181), ('Philadelphia', 97)],
    'Philadelphia': [('New_York', 97), ('Baltimore', 101), ('Pittsburgh', 305)],
    'Baltimore': [('Philadelphia', 101), ('Pittsburgh', 247)],
    'Portland': [('Boston', 107)]
}

heuristics = {
    'Boston': 0, 'Providence': 50, 'Portland': 107, 'New_York': 215,
    'Philadelphia': 270, 'Baltimore': 360, 'Syracuse': 260, 'Buffalo': 400,
    'Pittsburgh': 470, 'Cleveland': 550, 'Columbus': 640, 'Detroit': 610,
    'Indianapolis': 780, 'Chicago': 860
}

def greedy_best_first(start, goal):
    visited = []
    # Priority Queue store: (heuristic, current_node, path)
    queue = [(heuristics[start], start, [start])]
    
    while queue:
        # Sort by h(n)
        queue.sort()
        h, current, path = queue.pop(0)
        
        if current in visited: continue
        visited.append(current)
        
        if current == goal:
            return path, visited
        
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                queue.append((heuristics[neighbor], neighbor, path + [neighbor]))
    return None

def a_star(start, goal):
    visited = []
    # Priority Queue store: (f_score, g_score, current_node, path)
    queue = [(heuristics[start], 0, start, [start])]
    
    while queue:
        # Sort by f(n) = g(n) + h(n)
        queue.sort()
        f, g, current, path = queue.pop(0)
        
        if current in visited: continue
        visited.append(current)
        
        if current == goal:
            return path, visited
        
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                queue.append((new_f, new_g, neighbor, path + [neighbor]))
    return None

# Results
g_path, g_visited = greedy_best_first('Chicago', 'Boston')
a_path, a_visited = a_star('Chicago', 'Boston')

print(f"Greedy Best First Path: {' -> '.join(g_path)}")
print(f"Cities Explored: {len(g_visited)} ({', '.join(g_visited)})")
print("-" * 30)
print(f"A* Search Path: {' -> '.join(a_path)}")
print(f"Cities Explored: {len(a_visited)} ({', '.join(a_visited)})")