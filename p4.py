
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sum(x**2)

def DE(method):
    x = np.random.uniform(-5, 5, (40, 10))
    y = np.sum(x**2, axis=1)
    curve = [min(y)]

    for _ in range(200):
        best = x[y.argmin()].copy()

        for i in range(40):
            ids = np.delete(np.arange(40), i)
            a, b = x[np.random.choice(ids, 2, False)]

            if method == "rand/1":
                c = x[np.random.choice(np.setdiff1d(ids, []), 1)[0]]
                v = a + 0.8*(b-c)
            elif method == "best/1":
                v = best + 0.8*(a-b)
            else:
                v = x[i] + 0.8*(best-x[i]) + 0.8*(a-b)

            v = np.clip(v, -5, 5)
            m = np.random.rand(10) < 0.9
            m[np.random.randint(10)] = True
            trial = np.where(m, v, x[i])
            val = f(trial)

            if val < y[i]:
                x[i], y[i] = trial, val

        curve.append(min(y))

    return min(y), curve

np.random.seed(42)

for method in ["rand/1", "best/1", "current-to-best/1"]:
    value, curve = DE(method)
    print(f"{method} best value = {value:.6f}")
    plt.plot(curve, label=method)

plt.xlabel("Generation")
plt.ylabel("Best Objective Value")
plt.title("Differential Evolution Convergence")
plt.legend()
plt.grid()
plt.show()
