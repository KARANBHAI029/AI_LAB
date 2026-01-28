import random

class Agent:
    def __init__(self):
        self.table = {
            ('A', 'dirty'): 'clean',
            ('A', 'clean'): 'right',
            ('B', 'dirty'): 'clean',
            ('C', 'dirty'): 'clean',
            ('C', 'clean'): 'left'
        }

    def decide(self, loc, state):
        if (loc, state) in self.table:
            return self.table[(loc, state)]
        
        if loc == 'B' and state == 'clean':
            r = random.randint(0, 1)
            if r == 0:
                return 'right'
            else:
                return 'left'

def main():
    rooms = {'A': 'dirty', 'B': 'dirty', 'C': 'dirty'}
    curr = 'A'
    cost = 0
    
    bot = Agent()
    
    print("Step | Loc | State  | Action | New Loc")
    print("-" * 40)

    for i in range(1, 11):
        state = rooms[curr]
        act = bot.decide(curr, state)
        
        prev = curr
        
        if act == 'clean':
            rooms[curr] = 'clean'
            cost += 10
        elif act == 'right':
            cost -= 1
            if curr == 'A': curr = 'B'
            elif curr == 'B': curr = 'C'
        elif act == 'left':
            cost -= 1
            if curr == 'C': curr = 'B'
            elif curr == 'B': curr = 'A'
            
        print(f"{i:<4} | {prev:<3} | {state:<6} | {act:<6} | {curr}")

    print("-" * 40)
    print("Total Performance:", cost)

main()