
import numpy as np, random, math
import matplotlib.pyplot as plt

np.random.seed(42)
random.seed(42)

c = np.random.rand(30, 2) * 100
d = np.sqrt(((c[:, None] - c[None, :])**2).sum(2))
r = list(range(30))
random.shuffle(r)

def cost(r):
    return sum(d[r[i], r[(i+1)%30]] for i in range(30))

cur = best = cost(r)
b = r[:]
h = [best]
T = 100

for _ in range(20000):
    a, z = sorted(random.sample(range(30), 2))
    nr = r[:a] + r[a:z+1][::-1] + r[z+1:]
    nc = cost(nr)

    if nc < cur or random.random() < math.exp((cur-nc)/T):
        r, cur = nr, nc
        if cur < best:
            best, b = cur, r[:]

    h.append(best)
    T *= 0.995
    if T < 1e-3:
        break

print(f"Best Tour Length: {best:.2f}")

plt.plot(h)
plt.xlabel("Iteration")
plt.ylabel("Best Tour Length")
plt.title("Simulated Annealing Progress")
plt.grid()
plt.show()

b.append(b[0])
plt.plot(c[b, 0], c[b, 1], '-o')
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Final TSP Tour (Length = {best:.2f})")
plt.show()
