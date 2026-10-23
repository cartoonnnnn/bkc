
import numpy as np
import matplotlib.pyplot as plt

def sphere(x):
    return np.sum(x**2)

def BBO(func, dim=5, pop_size=20, generations=100, bounds=(-5,5), mutation_rate=0.05):
    lo, hi = bounds
    pop = np.random.uniform(lo, hi, (pop_size, dim))
    fit = np.array([func(x) for x in pop])
    curve = []

    for _ in range(generations):
        idx = np.argsort(fit)
        pop, fit = pop[idx], fit[idx]
        f = fit.max() - fit
        f = f/(f.max()+1e-9) if f.max() else np.ones(pop_size)
        lam, mu = 1-f, f
        p = mu/mu.sum() if mu.sum() else None
        new = pop.copy()

        for i in range(pop_size):
            for j in range(dim):
                if np.random.rand() < lam[i]:
                    donor = np.random.choice(pop_size, p=p)
                    new[i,j] = pop[donor,j]
            if np.random.rand() < mutation_rate:
                new[i] = np.random.uniform(lo, hi, dim)

        nf = np.array([func(x) for x in new])
        pop = np.vstack((pop,new))
        fit = np.concatenate((fit,nf))
        idx = np.argsort(fit)[:pop_size]
        pop, fit = pop[idx], fit[idx]
        curve.append(fit[0])

    return pop[0], fit[0], curve

np.random.seed(42)
best, value, curve = BBO(sphere, generations=200)

print("Best Solution:", best)
print("Best Fitness:", value)

plt.plot(curve)
plt.title("BBO Convergence Curve (Sphere Function)")
plt.xlabel("Generations")
plt.ylabel("Best Fitness Value")
plt.show()
