
import random

def fitness(s):
    n = len(s)
    pairs = n * (n-1) // 2
    attacks = sum(s[i] == s[j] or abs(s[i]-s[j]) == j-i
                  for i in range(n) for j in range(i+1, n))
    return pairs - attacks

def hill_climb(n):
    s = [random.randrange(n) for _ in range(n)]
    while True:
        b = max([s[:c]+[r]+s[c+1:] for c in range(n)
                 for r in range(n) if r != s[c]], key=fitness)
        if fitness(b) <= fitness(s):
            return s
        s = b

n = 8
goal = n*(n-1)//2
for attempt in range(1, 1001):
    solution = hill_climb(n)
    if fitness(solution) == goal:
        break

print("Attempts:", attempt)
print("Fitness:", fitness(solution))
for row in range(n):
    print(" ".join("Q" if solution[col] == row else "." for col in range(n)))
