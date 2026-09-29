import random, math
import numpy as np
import matplotlib.pyplot as plt

def mc_sim_pi(N):  # N is an integer
    cnt_in_circle = 0
    for i in range(N):
        x = round(random.uniform(-1,1), 2)
        y = round(random.uniform(-1,1), 2)
        r_2 = x**2 + y**2
        if r_2 <= 1:
            cnt_in_circle += 1
    sim_pi = 4 * cnt_in_circle / N
    return sim_pi

pi = math.pi
x_axis = np.geomspace(1e2, 1e6, 200)
y_axis = []
for j in x_axis:
    abs_error = abs(pi - mc_sim_pi(int(j)))
    y_axis.append(abs_error)

plt.semilogx(x_axis, y_axis, "o-", markersize=3)
plt.xlabel("Sample size N")
plt.ylabel(r"Absolute error $|\hat{\pi}-\pi|$")
plt.title(r"Monte Carlo estimation of $\pi$")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("./HW_1/Source/error_curve.png", dpi=200)
