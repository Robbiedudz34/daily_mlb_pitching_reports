import numpy as np

# Define the first pair of polar coordinates
theta1_deg, r1 = 0, 325
# Define the second pair of polar coordinates
theta2_deg, r2 = 45, 400

# Convert degrees to radians
theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

# Convert to Cartesian coordinates
x1 = r1 * np.cos(theta1)
y1 = r1 * np.sin(theta1)
x2 = r2 * np.cos(theta2)
y2 = r2 * np.sin(theta2)

# Compute line coefficients A*x + B*y = C
A = y1 - y2
B = x2 - x1
C = A * x1 + B * y1

# Also derive normalized form: r = X / (sinθ + Y cosθ)
X = C / B
Y = A / B

# print r
def smart_round(val, max_decimals=7):
    s = f"{val:.{max_decimals}f}".rstrip('0').rstrip('.')
    return s

print(f"Polar line equation: return {smart_round(X)} / (np.sin(theta) + ({smart_round(Y)} * cos(θ)))")
