import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()  # Create a PyWiFi object
    iface = wifi.interfaces()[0]  # Get the first wireless interface

    iface.scan()  # Start scanning
    time.sleep(5)  # Wait for scan results

    scan_results = iface.scan_results()  # Get scan results
    networks = []
    
    for network in scan_results:
        network_info = {
            "SSID": network.ssid,
            "BSSID": network.bssid,
            "Signal": network.signal,
            "Frequency": network.freq,
            "Auth": network.akm
        }
        networks.append(network_info)
    
    return networks

# Run the scan
networks = scan_wifi()
print("Available Wi-Fi Networks:")
for idx, network in enumerate(networks, 1):
    print(f"{idx}. SSID: {network['SSID']}, Signal: {network['Signal']} dBm, Frequency: {network['Frequency']} MHz")

