import numpy as np
import matplotlib.pyplot as plt

# Parameters
wavelength = 500e-9  # Wavelength in meters (500 nm)
slit_width = 0.0001  # Slit width in meters (0.1 mm)
slit_distance = 0.001  # Distance between slits in meters (1 mm)
theta = np.linspace(-0.01, 0.01, 1000)  # Angle range in radians

# Intensity Calculation
beta = (np.pi * slit_width * np.sin(theta)) / wavelength
delta = (np.pi * slit_distance * np.sin(theta)) / wavelength
intensity = (np.cos(delta) ** 2) * ((np.sin(beta) / beta) ** 2)
intensity = np.nan_to_num(intensity)  # Handle division by zero

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(theta, intensity, label="Double Slit Interference")
plt.title("Double Slit Interference Pattern")
plt.xlabel("Angle (radians)")
plt.ylabel("Normalized Intensity")
plt.grid(True)
plt.legend()
plt.show()
