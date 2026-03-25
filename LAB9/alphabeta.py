import math

# A simple list of leaf values (outcomes) for a tree of depth 3
# 2^3 = 8 leaf nodes
scores = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, node_index, is_maximizing, alpha, beta):
    # Base case: leaf node reached
    if depth == 3:
        return scores[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2): # Binary tree (2 branches)
            val = minimax(depth + 1, node_index * 2 + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Pruning condition
            if beta <= alpha:
                print(f"  Pruning at Maximizer (Depth {depth})")
                break
        return best
    
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Pruning condition
            if beta <= alpha:
                print(f"  Pruning at Minimizer (Depth {depth})")
                break
        return best

# Execution
print("Starting Minimax with Alpha-Beta Pruning...")
result = minimax(0, 0, True, -math.inf, math.inf)
print(f"The optimal value found is: {result}")