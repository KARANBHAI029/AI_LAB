def resolve(ci, cj):
    resolvents = set()
    for lit in ci:
        neg_lit = lit[1:] if lit.startswith('~') else '~' + lit
        if neg_lit in cj:
            res = (ci - {lit}) | (cj - {neg_lit})
            resolvents.add(frozenset(res))
    return resolvents

def resolution(clauses):
    kb = {frozenset(c) for c in clauses}
    
    while True:
        new = set()
        pairs = [(ci, cj) for ci in kb for cj in kb if ci != cj]
        
        for ci, cj in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return True
            new.update(resolvents)
            
        if new.issubset(kb):
            return False
            
        kb.update(new)

kb_3a = [{'P', 'Q'}, {'~P', 'R'}, {'~Q', 'S'}, {'~R', 'S'}, {'~S'}]
print("Result 3a:", resolution(kb_3a))

kb_3b = [{'~P', 'Q'}, {'~Q', 'R'}, {'~S', '~R'}, {'P'}, {'~S'}]
print("Result 3b:", resolution(kb_3b))
