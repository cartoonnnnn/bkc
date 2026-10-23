import numpy as np
import random
import math
import matplotlib.pyplot as plt


def distance(c):
    d = c[:, None] - c[None, :]
    return np.sqrt((d ** 2).sum(axis=2))


def length(r, d):
    return sum(d[r[i], r[(i + 1) % len(r)]] for i in range(len(r)))


def swap(r):
    a, b = sorted(random.sample(range(len(r)), 2))
    return r[:a] + r[a:b + 1][::-1] + r[b + 1:]


def SA(coords, T=100, Tmin=1e-3, alpha=0.995, iters=20000):

    d = distance(coords)
    r = list(range(len(coords)))

    random.shuffle(r)

    best = r[:]
    cost = current = length(r, d)

    history = [cost]

    for _ in range(iters):

        new = swap(r)
        nc = length(new, d)
        delta = nc - current

        if delta < 0 or random.random() < math.exp(-delta / T):
            r, current = new, nc

            if current < cost:
                best, cost = r[:], current

        history.append(cost)

        T *= alpha

        if T < Tmin:
            break

    return best, cost, history


np.random.seed(42)
random.seed(42)

coords = np.random.rand(30, 2) * 100

route, cost, history = SA(coords)

print(f"Best Tour Length: {cost:.2f}")


plt.figure(figsize=(7, 4))
plt.plot(history)
plt.xlabel("Iteration")
plt.ylabel("Best Tour Length")
plt.title("Simulated Annealing Progress")
plt.grid(True)
plt.show()


route = route + [route[0]]

x = coords[route, 0]
y = coords[route, 1]

plt.figure(figsize=(6, 6))
plt.plot(x, y, '-o')
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Final TSP Tour (Length = {cost:.2f})")
plt.show()
