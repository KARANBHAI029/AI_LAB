import pprint

def get_erratic_results(state, action):
    pos, sA, sB = state
    
    if action == "Suck":
        if pos == "A":
            if sA == "Dirty":
                return [("A", "Clean", sB), ("A", "Clean", "Clean")]
            else:
                return [("A", "Clean", sB), ("A", "Dirty", sB)]
        elif pos == "B":
            if sB == "Dirty":
                return [("B", sA, "Clean"), ("B", "Clean", "Clean")]
            else:
                return [("B", sA, "Clean"), ("B", sA, "Dirty")]
                
    if action == "Move_Left":
        return [("A", sA, sB)]
    if action == "Move_Right":
        return [("B", sA, sB)]
    
    return [state]

def and_or_search(state):
    return or_search(state, [])

def or_search(state, path):
    if state[1] == "Clean" and state[2] == "Clean":
        return "Goal_Reached"
    
    if state in path:
        return None

    actions = ["Suck", "Move_Left", "Move_Right"]
    
    for action in actions:
        outcomes = get_erratic_results(state, action)
        plan = and_search(outcomes, path + [state])
        if plan:
            return {action: plan}
            
    return None

def and_search(states, path):
    results = {}
    for s in states:
        res = or_search(s, path)
        if res is None:
            return None
        results[s] = res
    return results

initial_state = ("A", "Dirty", "Dirty")
strategy = and_or_search(initial_state)

print("Final Contingency Plan:")
pprint.pprint(strategy)