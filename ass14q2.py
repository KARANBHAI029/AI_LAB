def backward_chaining(rules, facts, query, visited=None):
    if visited is None:
        visited = set()
        
    if query in facts:
        return True
        
    if query in visited:
        return False
        
    visited.add(query)
    
    for premises, conclusion in rules:
        if conclusion == query:
            if all(backward_chaining(rules, facts, p, visited.copy()) for p in premises):
                return True
                
    return False

rules_2a = [(['P'], 'Q'), (['R'], 'Q'), (['A'], 'P'), (['B'], 'R')]
facts_2a = {'A', 'B'}
print("Result 2a:", backward_chaining(rules_2a, facts_2a, 'Q'))

rules_2b = [(['A'], 'B'), (['B', 'C'], 'D'), (['E'], 'C')]
facts_2b = {'A', 'E'}
print("Result 2b:", backward_chaining(rules_2b, facts_2b, 'D'))
