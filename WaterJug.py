from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque([(0, 0, [])])
    
    while queue:
        a, b, path = queue.popleft()
        
        if a == target or b == target:
            return path + [(f"Reached {target} in {'Jug 1' if a == target else 'Jug 2'}", (a, b))]
            
        if (a, b) in visited:
            continue
        visited.add((a, b))

        next_states = [
            (cap1, b, path + [("Fill Jug 1", (cap1, b))]),
            (a, cap2, path + [("Fill Jug 2", (a, cap2))]),
            (0, b, path + [("Empty Jug 1", (0, b))]),
            (a, 0, path + [("Empty Jug 2", (a, 0))]),
            (a - min(a, cap2 - b), b + min(a, cap2 - b), path + [("Pour Jug 1 -> Jug 2", (a - min(a, cap2 - b), b + min(a, cap2 - b)))]),
            (a + min(b, cap1 - a), b - min(b, cap1 - a), path + [("Pour Jug 2 -> Jug 1", (a + min(b, cap1 - a), b - min(b, cap1 - a)))]),
        ]
        
        for state in next_states:
            if (state[0], state[1]) not in visited:
                queue.append(state)
    
    return None

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target % (__import__('math').gcd(jug1, jug2)) != 0:
    print("No solution possible")
else:
    solution = water_jug_bfs(jug1, jug2, target)
    print("\nSolution Steps:" if solution else "No solution found")
    for step, (action, state) in enumerate(solution, 1):
        print(f"{step}. {action} -> State: {state}")