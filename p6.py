import numpy as np
import matplotlib.pyplot as plt

def sphere(x):
    return np.sum(x**2)

def FFA(func, dim=5, pop_size=20, generations=100, bounds=(-5,5),
        alpha=0.25, beta0=1.0, gamma=1.0, alpha_decay=0.97):
    lo, hi = bounds
    x = np.random.uniform(lo, hi, (pop_size, dim))
    y = np.array([func(p) for p in x])
    h, a = [], alpha

    for _ in range(generations):
        new = x.copy()
        for i in range(pop_size):
            c = x[i].copy()
            for j in range(pop_size):
                if y[j] < y[i]:
                    d = np.sum((x[i]-x[j])**2)
                    b = beta0*np.exp(-gamma*d)
                    c += b*(x[j]-c) + a*(hi-lo)*(np.random.rand(dim)-0.5)
            new[i] = np.clip(c, lo, hi)

        z = np.array([func(p) for p in new])
        x = np.vstack((x, new))
        y = np.concatenate((y, z))
        k = np.argsort(y)[:pop_size]
        x, y = x[k], y[k]
        h.append(y[0])
        a *= alpha_decay

    return x[0], y[0], h

np.random.seed(42)
best, value, curve = FFA(sphere, generations=200)

print("Best Solution:", best)
print("Best Fitness:", value)
plt.plot(curve)
plt.title("FFA Convergence Curve (Sphere Function)")
plt.xlabel("Generations")
plt.ylabel("Best Fitness Value")
plt.grid(True)
plt.show()
