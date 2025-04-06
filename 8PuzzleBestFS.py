import heapq

def h(s, g):
    return sum(1 for i in range(9) if s[i] != g[i] and s[i] != 0)

def moves(s):
    i = s.index(0)
    r, c = divmod(i, 3)
    directions = [(-1,0,'Up'), (1,0,'Down'), (0,-1,'Left'), (0,1,'Right')]
    for dr, dc, move in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            t = list(s)
            t[i], t[j] = t[j], t[i]
            yield tuple(t), move

def bfs(start, goal):
    q = [(h(start, goal), start)]
    seen = {start: (None, None)}
    while q:
        _, cur = heapq.heappop(q)
        if cur == goal:
            path = []
            while cur:
                parent, move = seen[cur]
                path.append((cur, move))
                cur = parent
            return path[::-1]
        for n, move in moves(cur):
            if n not in seen:
                seen[n] = (cur, move)
                heapq.heappush(q, (h(n, goal), n))
    return []

def is_valid(p):
    return sorted(p) == list(range(9))

start = tuple(map(int, input("Enter start (0-8, space-separated): ").split()))
goal = tuple(map(int, input("Enter goal (0-8, space-separated): ").split()))

if not (is_valid(start) and is_valid(goal)):
    print("Invalid input! Use numbers 0 to 8 exactly once.")
else:
    path = bfs(start, goal)
    if not path:
        print("No solution found.")
    else:
        for i, (p, move) in enumerate(path):
            print(f"Step {i}: {'Start' if move is None else f'Move {move}'}")
            print(p[0:3])
            print(p[3:6])
            print(p[6:])
            print()