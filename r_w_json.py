
import json
req_file = "C:\\Users\\KARTHIK\\Desktop\\json\\learn.json"
fo=open(req_file,'r')
print((json.load(fo)))
fo.close()

import json

my_dic = {'squadName': 'super hero squad', 'homeTown': 'nick City', 'formed': 2022, 'secretBase': 'Super tower', 'active': True, 'members': [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes'}]}
req_file ="C:\\Users\\KARTHIK\\Desktop\\json\\new.json"
fo=open(req_file ,'w')
json.dump(my_dic,fo,indent=4)
fo.close()


