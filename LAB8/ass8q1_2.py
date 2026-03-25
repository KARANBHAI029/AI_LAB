import random

# Distance Matrix (A=0, B=1, ..., H=7)
dist_matrix = [
    [0, 10, 15, 20, 25, 30, 35, 40],
    [12, 0, 35, 15, 20, 25, 30, 45],
    [25, 30, 0, 10, 40, 20, 15, 35],
    [18, 25, 12, 0, 15, 30, 20, 10],
    [22, 18, 28, 20, 0, 15, 25, 30],
    [35, 22, 18, 28, 12, 0, 40, 20],
    [30, 35, 22, 18, 28, 32, 0, 15],
    [40, 28, 35, 22, 18, 25, 12, 0]
]

def get_cost(path):
    total = 0
    for i in range(len(path)):
        total += dist_matrix[path[i]][path[(i + 1) % len(path)]]
    return total

def get_neighbors(path):
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = list(path)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def local_beam_search(k, iters=100):
    cities = list(range(8))
    current_states = []
    for _ in range(k):
        state = list(cities)
        random.shuffle(state)
        current_states.append(state)
    
    for _ in range(iters):
        candidates = []
        for state in current_states:
            candidates.extend(get_neighbors(state))
        candidates.sort(key=lambda x: get_cost(x))
        current_states = candidates[:k]
    
    return current_states[0], get_cost(current_states[0])

def crossover(p1, p2, points=1):
    size = len(p1)
    child = [-1] * size
    if points == 1:
        cp = random.randint(1, size - 2)
        child[:cp] = p1[:cp]
    else:
        cp1, cp2 = sorted(random.sample(range(size), 2))
        child[cp1:cp2] = p1[cp1:cp2]
    
    p2_idx = 0
    for i in range(size):
        if child[i] == -1:
            while p2[p2_idx] in child:
                p2_idx += 1
            child[i] = p2[p2_idx]
    return child

def genetic_algorithm(points, pop_size=20, gens=100):
    cities = list(range(8))
    pop = []
    for _ in range(pop_size):
        state = list(cities)
        random.shuffle(state)
        pop.append(state)
    
    for _ in range(gens):
        pop.sort(key=lambda x: get_cost(x))
        next_gen = pop[:2]
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(pop[:10], 2)
            child = crossover(p1, p2, points)
            if random.random() < 0.2: # Mutation
                idx1, idx2 = random.sample(range(8), 2)
                child[idx1], child[idx2] = child[idx2], child[idx1]
            next_gen.append(child)
        pop = next_gen
    
    return pop[0], get_cost(pop[0])

print("--- Local Beam Search ---")
for k in [3, 5, 10]:
    p, c = local_beam_search(k)
    print(f"k={k}: Path {p}, Cost {c}")

print("\n--- Genetic Algorithm ---")
for pts in [1, 2]:
    p, c = genetic_algorithm(pts)
    print(f"Crossover {pts}: Path {p}, Cost {c}")