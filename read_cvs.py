import csv
req_file ="C:\\Users\\KARTHIK\\Desktop\\info\\info.csv"
fo=open(req_file,'r')
content  = csv.reader(fo)
for each in content:
  print(each)
fo.close()


