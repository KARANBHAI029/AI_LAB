def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(start, end, maze):
    q = [start]
    parent = {}
    g = {start: 0}
    f = {start: dist(start, end)}

    while len(q) > 0:
        curr = q[0]
        for node in q:
            if f.get(node, 999) < f.get(curr, 999):
                curr = node

        if curr == end:
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            path.reverse()
            return path

        q.remove(curr)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            nr = curr[0] + move[0]
            nc = curr[1] + move[1]

            if 0 <= nr <= 4 and 0 <= nc <= 4:
                if maze[nr][nc] != 1:
                    temp_g = g[curr] + 1
                    if temp_g < g.get((nr, nc), 999):
                        parent[(nr, nc)] = curr
                        g[(nr, nc)] = temp_g
                        f[(nr, nc)] = temp_g + dist((nr, nc), end)
                        if (nr, nc) not in q:
                            q.append((nr, nc))
    return []

maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

start = None
goals = []

for r in range(5):
    for c in range(5):
        if maze[r][c] == 2:
            start = (r, c)
        if maze[r][c] == 3:
            goals.append((r, c))

all_steps = [start]
curr_pos = start

while len(goals) > 0:
    best_path = []
    best_goal = None
    
    for goal in goals:
        p = find_path(curr_pos, goal, maze)
        if best_path == [] or len(p) < len(best_path):
            best_path = p
            best_goal = goal
            
    if len(best_path) > 1:
        for step in best_path[1:]:
            all_steps.append(step)
            
    curr_pos = best_goal
    goals.remove(best_goal)

for s in all_steps:
    print(s)