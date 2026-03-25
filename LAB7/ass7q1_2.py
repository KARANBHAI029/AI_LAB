import random
import math

def get_heuristic(state):
    h = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j]:
                h += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]

def get_all_neighbors(state):
    neighbors = []
    for col in range(8):
        for row in range(8):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def get_random_neighbor(state):
    neighbor = list(state)
    col = random.randint(0, 7)
    row = random.randint(0, 7)
    while neighbor[col] == row:
        row = random.randint(0, 7)
    neighbor[col] = row
    return neighbor

def steepest_ascent(initial_state):
    current_state = initial_state
    current_h = get_heuristic(current_state)
    steps = 0
    initial_h = current_h
    
    while True:
        neighbors = get_all_neighbors(current_state)
        best_neighbor = None
        best_h = current_h
        
        for neighbor in neighbors:
            h = get_heuristic(neighbor)
            if h < best_h:
                best_h = h
                best_neighbor = neighbor
                
        if best_h >= current_h:
            break
            
        current_state = best_neighbor
        current_h = best_h
        steps += 1
        
    status = "Solved" if current_h == 0 else "Fail"
    return initial_h, current_h, steps, status

def first_choice(initial_state):
    current_state = initial_state
    current_h = get_heuristic(current_state)
    steps = 0
    initial_h = current_h
    max_attempts = 100
    
    while current_h > 0:
        found_better = False
        for _ in range(max_attempts):
            neighbor = get_random_neighbor(current_state)
            h = get_heuristic(neighbor)
            if h < current_h:
                current_state = neighbor
                current_h = h
                steps += 1
                found_better = True
                break
                
        if not found_better:
            break
            
    status = "Solved" if current_h == 0 else "Fail"
    return initial_h, current_h, steps, status

def random_restart():
    total_steps = 0
    restarts = 0
    while True:
        initial_state = generate_random_board()
        _, final_h, steps, _ = steepest_ascent(initial_state)
        total_steps += steps
        if final_h == 0:
            break
        restarts += 1
        
    return "N/A", 0, total_steps, f"Solved in {restarts} restarts"

def simulated_annealing(initial_state):
    current_state = initial_state
    current_h = get_heuristic(current_state)
    steps = 0
    initial_h = current_h
    
    T = 100.0
    cooling_rate = 0.95
    
    while T > 0.01 and current_h > 0:
        neighbor = get_random_neighbor(current_state)
        next_h = get_heuristic(neighbor)
        delta_e = next_h - current_h
        
        if delta_e < 0:
            current_state = neighbor
            current_h = next_h
        else:
            probability = math.exp(-delta_e / T)
            if random.random() < probability:
                current_state = neighbor
                current_h = next_h
                
        T *= cooling_rate
        steps += 1
        
    status = "Solved" if current_h == 0 else "Fail"
    return initial_h, current_h, steps, status

def run_experiments():
    boards = [generate_random_board() for _ in range(50)]
    
    algorithms = {
        "Steepest Ascent": steepest_ascent,
        "First Choice": first_choice,
        "Simulated Annealing": simulated_annealing
    }
    
    results = {algo: {"solved": 0, "steps": 0} for algo in algorithms}
    
    for algo_name, algo_func in algorithms.items():
        print(f"\n--- {algo_name} (First 10 Runs) ---")
        print(f"{'Run':<5} | {'Init H':<6} | {'Final H':<7} | {'Steps':<6} | {'Status'}")
        print("-" * 50)
        
        for i, board in enumerate(boards):
            i_h, f_h, s, stat = algo_func(board)
            if f_h == 0: results[algo_name]["solved"] += 1
            results[algo_name]["steps"] += s
            
            if i < 10:
                print(f"{i+1:<5} | {i_h:<6} | {f_h:<7} | {s:<6} | {stat}")
        print("...")

    print("\n--- Random Restart (10 Runs) ---")
    print(f"{'Run':<5} | {'Steps':<6} | {'Status'}")
    print("-" * 40)
    rr_steps = 0
    for i in range(10):
        _, _, s, stat = random_restart()
        rr_steps += s
        print(f"{i+1:<5} | {s:<6} | {stat}")

    print("\n### Final Comparison (Averaged over 50 runs) ###")
    for algo, data in results.items():
        print(f"{algo:<20}: Solved {data['solved']:<2}/50 ({(data['solved']/50)*100:>4}%) | Avg Steps: {data['steps']/50:.1f}")
    print(f"{'Random Restart':<20}: Solved 10/10 (100.0%) | Avg Steps: {rr_steps/10:.1f} (Includes restarts)")

if __name__ == "__main__":
    run_experiments()