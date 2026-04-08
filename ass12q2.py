def run_logic_filter(variables_list, possible_options, connected_neighbors, max_traces=0):
    checking_queue = [(current_var, neighbor) for current_var in variables_list for neighbor in connected_neighbors[current_var]]
    trace_history = []
    trace_counter = 0
    
    def narrow_down_options(var_a, var_b):
        did_we_change_anything = False
        options_to_drop = set()
        for option_a in possible_options[var_a]:
            if all(option_a == option_b for option_b in possible_options[var_b]):
                options_to_drop.add(option_a)
                did_we_change_anything = True
        for dropped in options_to_drop:
            possible_options[var_a].remove(dropped)
        return did_we_change_anything

    while checking_queue:
        var_a, var_b = checking_queue.pop(0)
        
        options_before = list(possible_options[var_a])
        was_revised = narrow_down_options(var_a, var_b)
        options_after = list(possible_options[var_a])
        
        if trace_counter < max_traces:
            if was_revised:
                trace_history.append(f"Checked {var_a} against {var_b}: options narrowed from {options_before} to {options_after}")
            else:
                trace_history.append(f"Checked {var_a} against {var_b}: no changes required")
            trace_counter += 1
            
        if was_revised:
            if len(possible_options[var_a]) == 0:
                return False, trace_history
            for next_neighbor in connected_neighbors[var_a]:
                if next_neighbor != var_b:
                    checking_queue.append((next_neighbor, var_a))
                    
    return True, trace_history

sudoku_layout_string = """
0 0 0 0 0 6 0 0 0
0 5 9 0 0 0 0 0 8
2 0 0 0 0 8 0 0 0
0 4 5 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0
0 0 6 0 0 3 0 5 0
0 0 0 0 0 7 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 5 0 0 0 2
"""
sudoku_board_numbers = []
for row_text in sudoku_layout_string.strip().split('\n'):
    sudoku_board_numbers.extend([int(number) for number in row_text.strip().split()])

grid_cell_ids = list(range(81))
cell_options = {}
for cell_id in range(81):
    if sudoku_board_numbers[cell_id] == 0:
        cell_options[cell_id] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        cell_options[cell_id] = [sudoku_board_numbers[cell_id]]

def map_sudoku_links():
    linked_cells = {cell_id: set() for cell_id in range(81)}
    for cell_id in range(81):
        row, col = cell_id // 9, cell_id % 9
        block_row, block_col = row // 3, col // 3
        for target_cell in range(81):
            if cell_id != target_cell:
                target_row, target_col = target_cell // 9, target_cell % 9
                target_block_row, target_block_col = target_row // 3, target_col // 3
                if row == target_row or col == target_col or (block_row == target_block_row and block_col == target_block_col):
                    linked_cells[cell_id].add(target_cell)
    return linked_cells

sudoku_links = map_sudoku_links()
total_options_at_start = sum(len(options) for options in cell_options.values())
total_rule_checks = sum(len(links) for links in sudoku_links.values())

print("--- THE SUDOKU PROBLEM ---")
print(f"Total rules mapped: {total_rule_checks}")

puzzle_survived, _ = run_logic_filter(grid_cell_ids, cell_options, sudoku_links, max_traces=0)

total_options_at_end = sum(len(options) for options in cell_options.values())
total_options_crossed_out = total_options_at_start - total_options_at_end

print(f"Impossible numbers crossed out: {total_options_crossed_out}")
has_empty_cells = any(len(options) == 0 for options in cell_options.values())
is_fully_solved = all(len(options) == 1 for options in cell_options.values())

print(f"Did any square run out of numbers entirely? {has_empty_cells}")
print(f"Did we find exactly one number for every square? {is_fully_solved}")

print("\nVisual map of remaining possibilities per square:")
print("+-------+-------+-------+")
for row_index in range(9):
    row_visual = []
    for col_index in range(9):
        row_visual.append(str(len(cell_options[row_index * 9 + col_index])))
    
    formatted_row = f"| {' '.join(row_visual[0:3])} | {' '.join(row_visual[3:6])} | {' '.join(row_visual[6:9])} |"
    print(formatted_row)
    
    if (row_index + 1) % 3 == 0:
        print("+-------+-------+-------+")