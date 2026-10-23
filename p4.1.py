import numpy as np
import matplotlib.pyplot as plt

def rastrigin(x):
    return 10 * x.size + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def differential_evolution(func, bounds, dim=10, population=40,
                           generations=300, F=0.8, CR=0.9):

    lo, hi = bounds

    pop = np.random.uniform(lo, hi, (population, dim))
    costs = np.array([func(x) for x in pop])

    history = [np.min(costs)]
    diversity = [np.mean(np.std(pop, axis=0))]

    for _ in range(generations):
        for i in range(population):
            choices = np.delete(np.arange(population), i)
            a, b, c = pop[np.random.choice(choices, 3, replace=False)]

            mutant = np.clip(a + F * (b - c), lo, hi)

            mask = np.random.rand(dim) < CR
            mask[np.random.randint(dim)] = True

            trial = np.where(mask, mutant, pop[i])
            trial_cost = func(trial)

            if trial_cost < costs[i]:
                pop[i] = trial
                costs[i] = trial_cost

        history.append(np.min(costs))
        diversity.append(np.mean(np.std(pop, axis=0)))

    best = np.argmin(costs)

    return pop[best], costs[best], history, diversity


np.random.seed(42)

best, value, history, diversity = differential_evolution(
    rastrigin, (-5.12, 5.12)
)

print("Best position:", best)
print(f"Best fitness: {value:.6f}")


plt.figure(figsize=(10, 5))
plt.plot(history)
plt.title("Differential Evolution Convergence")
plt.xlabel("Generation")
plt.ylabel("Best Objective Value")
plt.yscale("log")
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(diversity)
plt.title("Population Diversity over Generations")
plt.xlabel("Generation")
plt.ylabel("Average Std. Dev. of Population")
plt.grid(True)
plt.show()
