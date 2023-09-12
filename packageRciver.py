from scapy.all import *

# Define a callback function to process captured packets
def packet_callback(packet):
    print(packet.summary())

# Use the sniff() function to capture Wi-Fi packets
# Set the 'iface' parameter to specify the Wi-Fi interface to capture on
# Set the 'count' parameter to specify the number of packets to capture
# Set the 'prn' parameter to the callback function to process captured packets
sniff(iface="eth0", count=10, prn=packet_callback)
