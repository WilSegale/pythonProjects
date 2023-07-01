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
print("System Name:", system_name)
print("Node Name:", node_name)
print("Release:", release)
print("Version:", version)
print("Machine:", machine)
print("Processor:", processor)

