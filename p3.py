
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n, dim, iters = 30, 2, 200
x = np.random.uniform(-10, 10, (n, dim))
v = np.random.uniform(-1, 1, (n, dim))
p = x.copy()
pv = np.sum(p**2, axis=1)
g = p[np.argmin(pv)].copy()
gv = min(pv)
h = []

for i in range(1, iters + 1):
    v = 0.7*v + 1.5*np.random.rand(n, dim)*(p-x) + 1.5*np.random.rand(n, dim)*(g-x)
    x = np.clip(x+v, -10, 10)
    val = np.sum(x**2, axis=1)
    b = val < pv
    p[b], pv[b] = x[b], val[b]
    k = np.argmin(pv)

    if pv[k] < gv:
        g, gv = p[k].copy(), pv[k]

    h.append(gv)
    if (i-1) % 20 == 0 or i == iters:
        print(f"Iter {i}/{iters}, gBest = {gv:.6e}")

print("Result:")
print("Best position:", g)
print("Best value (fitness):", gv)

plt.plot(h)
plt.xlabel("Iteration")
plt.ylabel("gBest Fitness")
plt.title("PSO Convergence")
plt.grid()
plt.show()
