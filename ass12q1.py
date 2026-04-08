import copy

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

team_names = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
available_rooms = {team: ['R1', 'R2', 'R3'] for team in team_names}
clashing_teams = {
    'P1': ['P2', 'P3', 'P6'],
    'P2': ['P1', 'P3', 'P4'],
    'P3': ['P1', 'P2', 'P5'],
    'P4': ['P2', 'P6'],
    'P5': ['P3', 'P6'],
    'P6': ['P1', 'P4', 'P5']
}

print("--- THE SCHEDULING PROBLEM ---")
starting_rooms = copy.deepcopy(available_rooms)
is_schedule_valid, history_log = run_logic_filter(team_names, starting_rooms, clashing_teams, max_traces=5)

print("First five logic checks:")
for log_entry in history_log:
    print(log_entry)

print(f"\nIs the initial setup stable? {is_schedule_valid}")

print("\n--- FORCING TEAM 1 INTO ROOM 1 ---")
rooms_after_assignment = copy.deepcopy(available_rooms)
rooms_after_assignment['P1'] = ['R1']
is_still_valid, ignored_log = run_logic_filter(team_names, rooms_after_assignment, clashing_teams, max_traces=0)

print(f"Did the schedule survive the forced assignment? {is_still_valid}")
print("Remaining room options per team:")
for team, rooms in rooms_after_assignment.items():
    print(f"{team} -> {rooms}")