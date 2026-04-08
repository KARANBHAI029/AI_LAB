def is_valid_color(graph, node, color, color_assignment):
    for neighbor in graph[node]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(graph, colors, unassigned_nodes, color_assignment):
    if not unassigned_nodes:
        return True
    
    node = unassigned_nodes[0]
    
    for color in colors:
        if is_valid_color(graph, node, color, color_assignment):
            color_assignment[node] = color
            
            if solve_map_coloring(graph, colors, unassigned_nodes[1:], color_assignment):
                return True
            
            del color_assignment[node]
            
    return False


georgia_graph = {
    'Kuchchh': ['Patan', 'Surendranagar', 'Morbi'],
    'Banaskantha': ['Patan', 'Mehsana', 'Sabarkantha'],
    'Patan': ['Kuchchh', 'Banaskantha', 'Mehsana', 'Surendranagar'],
    'Mehsana': ['Banaskantha', 'Patan', 'Sabarkantha', 'Gandhinagar', 'Ahmedabad', 'Surendranagar'],
    'Sabarkantha': ['Banaskantha', 'Mehsana', 'Gandhinagar', 'Aravalli'],
    'Surendranagar': ['Kuchchh', 'Patan', 'Mehsana', 'Ahmedabad', 'Botad', 'Rajkot', 'Morbi'],
    'Morbi': ['Kuchchh', 'Surendranagar', 'Rajkot', 'Jamnagar'],
    'Rajkot': ['Morbi', 'Surendranagar', 'Botad', 'Amreli', 'Junagadh', 'Porbandar', 'Jamnagar'],
    'Jamnagar': ['Morbi', 'Rajkot', 'Porbandar']
}

available_colors = ['Red', 'Green', 'Blue', 'Yellow']
regions_to_color = list(georgia_graph.keys())
final_colors = {}

print("\n" + "="*80)
print(" "*20 + "GEOGRAPHIC MAP COLORING PROBLEM SOLVER")
print("="*80)

print("\n[SYSTEM INITIALIZATION]")
print(f"  > Total regions to color: {len(regions_to_color)}")
print(f"  > Colors available: {', '.join(available_colors)} ({len(available_colors)} colors)")
print(f"  > Graph density: {sum(len(neighbors) for neighbors in georgia_graph.values()) // 2} border connections")

print("\n[REGION ANALYSIS]")
for region in sorted(regions_to_color):
    neighbor_count = len(georgia_graph[region])
    print(f"  * {region:20} -> neighbors: {neighbor_count:2} regions")

print("\n" + "-"*80)
print("[CONSTRAINT PROPAGATION & BACKTRACKING SEARCH]")
print("-"*80)

iteration_count = [0]
max_depth = [0]

def solve_map_coloring_verbose(graph, colors, unassigned_nodes, color_assignment):
    iteration_count[0] += 1
    current_depth = len(color_assignment)
    if current_depth > max_depth[0]:
        max_depth[0] = current_depth
    
    if not unassigned_nodes:
        return True
    
    node = unassigned_nodes[0]
    neighbors_colored = [n for n in graph[node] if n in color_assignment]
    neighbor_colors = [color_assignment[n] for n in neighbors_colored]
    
    print(f"\n  [NODE {current_depth + 1}] Processing: {node}")
    print(f"    └─ Colored neighbors: {len(neighbors_colored)} / Neighbor colors used: {set(neighbor_colors)}")
    
    for color in colors:
        is_valid = is_valid_color(graph, node, color, color_assignment)
        status = "VALID" if is_valid else "CONFLICT"
        print(f"      -> Attempting {color:8} [{status}]")
        
        if is_valid:
            color_assignment[node] = color
            print(f"        # Assigned {color} to {node}")
            
            if solve_map_coloring_verbose(graph, colors, unassigned_nodes[1:], color_assignment):
                return True
            
            del color_assignment[node]
            print(f"        ! BACKTRACK from {node}")
    
    return False

if solve_map_coloring_verbose(georgia_graph, available_colors, regions_to_color, final_colors):
    print("\n" + "="*80)
    print(" "*25 + "✓ SOLUTION FOUND")
    print("="*80)
    
    print("\n[FINAL COLOR ASSIGNMENT]")
    for idx, (region, color) in enumerate(sorted(final_colors.items()), 1):
        color_indicator = "●" if color == "Red" else ("●" if color == "Green" else ("●" if color == "Blue" else "●"))
        print(f"  {idx:2}. {region:20} → {color:8} {color_indicator}")
    
    color_groups = {}
    for region, color in final_colors.items():
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(region)
    
    print("\n[COLOR DISTRIBUTION]")
    for color in available_colors:
        count = len(color_groups.get(color, []))
        print(f"  • {color:8}: {count:2} regions {color_groups.get(color, [])}")
    
    print("\n[ADJACENCY VERIFICATION]")
    all_valid = True
    for region, color in final_colors.items():
        for neighbor in georgia_graph[region]:
            if neighbor in final_colors:
                if final_colors[neighbor] == color:
                    print(f"  ✗ VIOLATION: {region} and {neighbor} both have {color}")
                    all_valid = False
    
    if all_valid:
        print(f"  ✓ All {len(final_colors)} regions verified - no adjacent regions share colors")
    
    print("\n[SEARCH STATISTICS]")
    print(f"  • Total iterations: {iteration_count[0]}")
    print(f"  • Maximum recursion depth: {max_depth[0]}")
    print(f"  • Backtracking operations: {iteration_count[0] - len(final_colors)}")
    
else:
    print("\n" + "="*80)
    print(" "*20 + "✗ NO SOLUTION FOUND - PROBLEM UNSOLVABLE")
    print("="*80)

print("\n" + "="*80 + "\n")