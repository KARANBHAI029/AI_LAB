import time

class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

def is_goal(state):
    return state == (0, 0, 0)

def is_valid(g, b):
    if g < 0 or g > 3 or b < 0 or b > 3: return False
    if g > 0 and g < b: return False
    g_right, b_right = 3 - g, 3 - b
    if g_right > 0 and g_right < b_right: return False
    return True

def expand(node):
    children = []
    g, b, boat = node.state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    op = -1 if boat == 1 else 1
    new_boat = 0 if boat == 1 else 1
    
    for mg, mb in moves:
        new_g = g + (op * mg)
        new_b = b + (op * mb)
        
        if is_valid(new_g, new_b):
            if node.parent and node.parent.state == (new_g, new_b, new_boat):
                continue
            
            child = Node((new_g, new_b, new_boat), node, (mg, mb), node.depth + 1)
            children.append(child)
            
    return children

def Depth_Limited_DFS(problem_initial_state, cutoff):
    frontier = [] 
    frontier.append(Node(problem_initial_state))
    
    nodes_explored = 0
    
    while frontier:
        node = frontier.pop()
        nodes_explored += 1
        
        if is_goal(node.state):
            return node, nodes_explored
        
        if node.depth == cutoff:
            continue
            
        for child in expand(node):
            frontier.append(child)
            
    return "failure", nodes_explored

def Iterative_Deepening_Search(initial_state):
    total_nodes_explored = 0
    
    for limit in range(21):
        result, count = Depth_Limited_DFS(initial_state, limit)
        total_nodes_explored += count
        
        if result != "failure":
            return result, total_nodes_explored
            
    return "failure", total_nodes_explored

if __name__ == "__main__":
    initial_state = (3, 3, 1)

    print("1(a) Running Depth Limited Search (Limit=3)")
    
    start_time = time.time()
    result_a, count_a = Depth_Limited_DFS(initial_state, 3)
    end_time = time.time()
    
    if result_a == "failure":
        print("Status: FAILED")
        print(f"Nodes Explored: {count_a}")
        print(f"Time Taken: {end_time - start_time:.6f} seconds")
        print("Approx. Time Complexity: O(b^L)")
    else:
        print("Status: SUCCESS")

    print("\n")
    print("1(b) Running Iterative Deepening Search")
    
    start_time = time.time()
    result_b, count_b = Iterative_Deepening_Search(initial_state)
    end_time = time.time()

    if result_b == "failure":
        print("Status: FAILED")
    else:
        print("Status: SUCCESS")
        print(f"Nodes Explored: {count_b}")
        print(f"Time Taken: {end_time - start_time:.6f} seconds")
        print("Approx. Time Complexity: O(b^d)")
        print(f"Goal Found at Depth: {result_b.depth}")
        print("Solution Path (Left Girls, Left Boys, Boat):")
        
        path = []
        curr = result_b
        while curr:
            path.append(curr.state)
            curr = curr.parent
        
        for i, step in enumerate(reversed(path)):
            print(f"Step {i}: {step}")
            
    print("\nCOMPARISON SUMMARY")
    print(f"{'Algorithm':<30} | {'Explored':<10} | {'Result':<10}")
    print(f"{'Depth Limited (L=3)':<30} | {count_a:<10} | {'Failed'}")
    print(f"{'Iterative Deepening':<30} | {count_b:<10} | {'Success'}")