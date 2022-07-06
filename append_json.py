import json
from os import path

req_file="C:\\Users\\KARTHIK\\Desktop\\json\\copy.json"

if path.isfile(req_file) is False:
  raise Exception("File not found")

with open(req_file) as fp:
 obj = json.load(fp)
print(obj)
obj.append({
    "Name": "Person_3",
    "Age": 33,
    "Email": "33@gmail.com"
})

# Verify updated list
print(obj)

with open(req_file, 'w') as file:
    json.dump(obj, file,
              indent=4,
              separators=(',', ': '))

print('Successfully appended to the JSON file')

