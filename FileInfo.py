import os

file_path = '/Users/admin/Desktop'
file_info = os.stat(file_path)

print('Size:', file_info.st_size)
print('Creation Time:', file_info.st_ctime)
print('Permissions:', oct(file_info.st_mode))
print('Name:', os.path.basename(file_path))
print('Is Directory:', os.path.isdir(file_path))
