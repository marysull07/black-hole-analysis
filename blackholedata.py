import matplotlib.pyplot as plt
import numpy as np

names = [
    "Cygnus X-1", "V404 Cygni", "GRO J1655-40",
    "Sagittarius A*", "M87*", "NGC 1277"
]

mass = [
    21, 9, 6.3,
    4.3e6, 6.5e9, 1.7e10
]

distance = [
    7200, 7800, 11200,
    26000, 53000000, 220000000
]

types = [
    "stellar", "stellar", "stellar",
    "supermassive", "supermassive", "supermassive"
]

# Convert to float arrays FIRST
distance = np.array(distance, dtype=float)
mass = np.array(mass, dtype=float)

# Add jitter BEFORE plotting
distance[:3] *= np.random.uniform(0.95, 1.05, size=3)
mass[:3] *= np.random.uniform(0.95, 1.05, size=3)

colors = ["blue" if t == "stellar" else "red" for t in types]

# Plot
plt.scatter(distance, mass, c=colors, s=120, edgecolors='black')

# Labels with arrows
for i, name in enumerate(names):
    plt.annotate(
        name,
        (distance[i], mass[i]),
        textcoords="offset points",
        xytext=(8,8),
        fontsize=8,
        arrowprops=dict(arrowstyle="->", lw=0.5)
    )

plt.yscale("log")

plt.xlabel("Distance (light years)")
plt.ylabel("Mass (solar masses, log scale)")
plt.title("Stellar vs Supermassive Black Holes")

plt.show()
