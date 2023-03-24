import pywifi
from pywifi import const
import time
import numpy as np
import matplotlib.pyplot as plt

def wifi_scan(target_ssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    data_points = []

    while True:
        iface.scan()
        time.sleep(3)  # Give some time for the scan to complete

        networks = iface.scan_results()

        # Find the target network
        target_network = None
        for network in networks:
            if network.ssid == target_ssid:
                target_network = network
                break

        if target_network:
            x = float(input("Enter X coordinate: "))
            y = float(input("Enter Y coordinate: "))

            data_point = (x, y, target_network.signal)
            data_points.append(data_point)
            print(f"Data point added: {data_point}")

            print("--------------------------------------------------")
        else:
            print(f"{target_ssid} not found in the scan results.")

        cont = input("Continue scanning? (y/n): ")
        if cont.lower() != 'y':
            break

    return data_points



if __name__ == "__main__":
    target_ssid = input("Enter the target SSID: ")
    data_points = wifi_scan(target_ssid)
    print("Collected data points:")
    print(data_points)


def create_heatmap(data_points):
    # Convert the data points into a grid
    x, y, signal_strength = zip(*data_points)
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    zi = plt.griddata((x, y), signal_strength, (xi[None, :], yi[:, None]), method='cubic')

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.contourf(xi, yi, zi, levels=15, cmap='inferno')
    plt.colorbar(label='Signal Strength (dBm)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Wi-Fi Signal Strength Heatmap')

    plt.show()
