"""
Beam Deflection Calculator
Based on formulas from:
American Forest & Paper Association - Beam Design Formulas
Figure 8:Concentrated Loads at any point

Author: Yvonne Rutendo Manyanda
Date: 23 February 2026
"""


import numpy as np
import matplotlib.pyplot as plt

# 1. Inputs
P = float(input("Enter the value of Load P (N): "))
l = float(input("Enter the length of the Beam (m): "))
a = float(input("Enter the distance 'a' from the left support (m): "))

# Calculation for EI (Assuming a 50mm x 50mm timber section as an example)
# It's good to keep this transparent
E = 200000 * (10**6) # Pa
I = (0.05 * 0.05**3) / 12 # m^4
EI = E * I

# 2. Logic & Math
b = l - a
R1 = P * b / l
R2 = P * a / l

x = np.linspace(0, l, 500) # 500 points for a smooth curve

# Shear Force calculation
V = np.zeros(500)
V[x < a] = R1
V[x >= a] = -R2

# Bending Moment calculation
M = np.where(x < a, R1 * x, R1 * x - P * (x - a))

# Deflection calculation (Formula from Figure 8)
D = np.zeros(500)
# Note: Using negative D so the plot shows the beam sagging downwards
D[x < a] = -((P * b * x[x < a]) / (6 * EI * l)) * (l**2 - b**2 - x[x < a]**2)
D[x >= a] = -((P * a * (l - x[x >= a])) / (6 * EI * l)) * (2 * l * x[x >= a] - x[x >= a]**2 - a**2)

# 3. Plotting the results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))
fig.tight_layout(pad=4.0)

# Shear Plot
ax1.fill_between(x, V, color="red", alpha=0.3)
ax1.plot(x, V, color="red", linewidth=2)
ax1.set_title(f"Shear Force Diagram (Load at {a}m)")
ax1.set_ylabel("Force (N)")
ax1.grid(True, alpha=0.3)

# Moment Plot
ax2.fill_between(x, M, color="green", alpha=0.3)
ax2.plot(x, M, color="green", linewidth=2)
ax2.set_title("Bending Moment Diagram")
ax2.set_ylabel("Moment (N-m)")
ax2.grid(True, alpha=0.3)

# Deflection Plot
ax3.plot(x, D, color="blue", linewidth=2)
ax3.axhline(y=0, color='black', linewidth=1) # Ground line
ax3.set_title("Deflected Shape (Elastic Curve)")
ax3.set_ylabel("Deflection (m)")
ax3.set_xlabel("Position (m)")
ax3.grid(True, alpha=0.3)

# Save the result as an image for GitHub
plt.savefig("beam_analysis_output.png")
print("Analysis complete. Plot saved as 'beam_analysis_output.png'")
plt.show()
