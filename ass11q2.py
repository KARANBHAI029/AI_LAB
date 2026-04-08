from itertools import permutations

def solve_crypto():
    print("\n" + "="*70)
    print("CRYPTARITHMETIC PUZZLE SOLVER - SEND + MORE = MONEY")
    print("="*70)
    print("\nInitializing search parameters...\n")
    
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    
    print(f"Letters to assign: {', '.join(letters)}")
    print(f"Total unique letters: {len(letters)}")
    print(f"Available digits: 0-9")
    print(f"Constraints: S ≠ 0 (first digit of SEND)")
    print(f"              M ≠ 0 (first digit of MONEY)")
    
    valid_found = 0
    
    print("\n" + "-"*70)
    print("SEARCHING FOR VALID SOLUTIONS...")
    print("-"*70 + "\n")
    
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        
        S = assignment['S']
        M = assignment['M']
        
        if S == 0 or M == 0:
            continue
        
        send = 1000 * S + 100 * assignment['E'] + 10 * assignment['N'] + assignment['D']
        more = 1000 * M + 100 * assignment['O'] + 10 * assignment['R'] + assignment['E']
        money = 10000 * M + 1000 * assignment['O'] + 100 * assignment['N'] + 10 * assignment['E'] + assignment['Y']
        
        if send + more == money:
            valid_found += 1
            
            print("\n" + "="*70)
            print(f"✓ VALID SOLUTION FOUND (Solution #{valid_found})")
            print("="*70)
            print(f"\n{'SEND':>15} = {send:>5}")
            print(f"{'+MORE':>15} = {more:>5}")
            print(f"{'─'*15}{' '*1}{'─'*5}")
            print(f"{'MONEY':>15} = {money:>5}\n")
            
            print("DIGIT ASSIGNMENTS:")
            for letter in sorted(assignment.keys()):
                print(f"  {letter} = {assignment[letter]}")
            
            print("\n" + "="*70 + "\n")
    
    print("="*70)
    print("SEARCH COMPLETED")
    print("="*70)
    print(f"\nTotal valid solutions found: {valid_found}\n")
    print("="*70 + "\n")

solve_crypto()