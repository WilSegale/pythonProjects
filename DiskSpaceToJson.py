import json
import shutil
total, used, free = shutil.disk_usage("/")

data = {"Total-GB": total // (2 ** 30), 
        "Used-GB": used // (2 ** 30),
        "Free-GB":free // (2 ** 30)
        }
json_data = json.dumps(data)

with open("DiskSpace.json", "w") as outfile:
    outfile.write(json_data)
print('Done it is located in the file called: DiskSpace.json')
