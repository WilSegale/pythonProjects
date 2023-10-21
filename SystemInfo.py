import platform

# Get the system information
system_info = platform.uname()

# Extract individual system details
system_name = system_info.system
node_name = system_info.node
release = system_info.release
version = system_info.version
machine = system_info.machine
processor = system_info.processor


# Print the system information
print("System Information:")
print(f"System Name: {system_name}")
print(f"Node Name: {node_name}")
print(f"Release: {release}")
print(f"Version: {version}")
print(f"Machine: {machine}")
print(f"Processor: {processor}")

