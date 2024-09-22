from DontEdit import *

file_path = os.path.expanduser("~/Desktop/")

file_info = os.stat(file_path)

print(f'Size: {file_info.st_size}')
print(f'Creation Time: {file_info.st_ctime}')
print(f'Permissions: {oct(file_info.st_mode)}')
print(f'Name: {os.path.basename(file_path)}')
print(f'Is Directory: {os.path.isdir(file_path)}')
