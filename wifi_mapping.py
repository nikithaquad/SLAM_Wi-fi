import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

data_points = [(0.0, 0.0, -37), (0.0, 3.0, -33), (0.0, 6.0, -14), (0.0, 10.0, -32), (3.0, 10.0, -32), (6.0, 10.0, -36), (10.0, 10.0, -38), (10.0, 6.0, -75), (10.0, 4.0, -34), (10.0, 2.0, -41), (10.0, 0.0, -76), (5.0, 0.0, -39), (0.0, 0.0, -44)]

def create_heatmap(data_points):
    # Convert the data points into a grid
    x, y, signal_strength = zip(*data_points)
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    zi = griddata((x, y), signal_strength, (xi[None, :], yi[:, None]), method='cubic')

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.contourf(xi, yi, zi, levels=15, cmap='inferno')
    plt.colorbar(label='Signal Strength (dBm)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Wi-Fi Signal Strength Heatmap')

    plt.show()

create_heatmap(data_points)
