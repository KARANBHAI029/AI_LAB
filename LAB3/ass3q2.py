def check_logic(track, obs, lever):
    if lever == 'active':
        return 'Red', 'Raise', 'On'
    
    if obs == 'detected':
        return 'Red', 'Raise', 'On'
        
    if track == 'detected':
        return 'Green', 'Lower', 'On'
        
    return 'Red', 'Raise', 'Off'

def main():
    inputs = [
        ['none', 'none', 'neutral'],
        ['detected', 'none', 'neutral'],
        ['detected', 'detected', 'neutral'],
        ['none', 'none', 'active'],
        ['detected', 'none', 'neutral']
    ]

    print(f"{'Step':<5} {'Track':<10} {'Object':<10} {'Lever':<10} {'Signal':<8} {'Gate':<8} {'Siren'}")
    print("-" * 65)

    for i in range(len(inputs)):
        track = inputs[i][0]
        obstacle = inputs[i][1]
        lever = inputs[i][2]
        
        sig, gate, siren = check_logic(track, obstacle, lever)
        
        print(f"{i+1:<5} {track:<10} {obstacle:<10} {lever:<10} {sig:<8} {gate:<8} {siren}")

main()