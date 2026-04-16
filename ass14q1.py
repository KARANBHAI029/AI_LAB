def forward_chaining(rules, facts, query):
    inferred = set(facts)
    
    if query in inferred:
        return True

    count = [len(premises) for premises, conclusion in rules]
    agenda = list(facts)
    
    while agenda:
        p = agenda.pop(0)
        
        for i, (premises, conclusion) in enumerate(rules):
            if p in premises:
                count[i] -= 1
                
                if count[i] == 0:
                    if conclusion == query:
                        return True
                    if conclusion not in inferred:
                        inferred.add(conclusion)
                        agenda.append(conclusion)
                        
    return False

rules_1a = [(['P'], 'Q'), (['L', 'M'], 'P'), (['A', 'B'], 'L')]
facts_1a = {'A', 'B', 'M'}
print("Result 1a:", forward_chaining(rules_1a, facts_1a, 'Q'))

rules_1b = [(['A'], 'B'), (['B'], 'C'), (['C'], 'D'), (['D', 'E'], 'F')]
facts_1b = {'A', 'E'}
print("Result 1b:", forward_chaining(rules_1b, facts_1b, 'F'))