import random
import matplotlib.pyplot as plt

# Simulate coin tosses
def coin_toss_simulation(n_tosses=1000):
    outcomes = {'Heads': 0, 'Tails': 0}
    for _ in range(n_tosses):
        toss = random.choice(['Heads', 'Tails'])
        outcomes[toss] += 1
    return outcomes

results = coin_toss_simulation(1000)

labels = list(results.keys())
values = list(results.values())

plt.bar(labels, values, color=['skyblue', 'lightcoral'])
plt.title("Coin Toss Simulation")
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
