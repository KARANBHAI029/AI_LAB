graph = {
    "Raj": ["Priya", "Sunil"],
    "Priya": ["Raj", "Aarav", "Akash", "Neha1"],
    "Aarav": ["Priya", "Neha2"],
    "Akash": ["Priya", "Sunil", "Neha2"],
    "Sunil": ["Raj", "Akash", "Sneha"],
    "Sneha": ["Sunil", "Rahul", "Maya"],
    "Rahul": ["Sneha", "Neha2", "Arjun1", "Pooja2"],
    "Neha1": ["Priya"],
    "Neha2": ["Aarav", "Akash", "Rahul"],
    "Arjun1": ["Rahul"],
    "Arjun2": ["Pooja2"],
    "Pooja2": ["Arjun2", "Rahul"],
    "Maya": ["Sneha"]
}

def get_bfs_tree(graph, start):
    visited = {start}
    queue = [start]
    tree = {}
    
    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if node not in tree:
                    tree[node] = []
                tree[node].append(neighbor)
                queue.append(neighbor)
    return tree

def get_dfs_tree(graph, start):
    visited = {start}
    tree = {}

    def construct(node):
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if node not in tree:
                    tree[node] = []
                tree[node].append(neighbor)
                construct(neighbor)
    
    construct(start)
    return tree

start_node = "Neha1"
bfs_res = get_bfs_tree(graph, start_node)
dfs_res = get_dfs_tree(graph, start_node)

print("BFS Tree:")
for parent, children in bfs_res.items():
    print(f"{parent} -> {children}")

print("\nDFS Tree:")
for parent, children in dfs_res.items():
    print(f"{parent} -> {children}")