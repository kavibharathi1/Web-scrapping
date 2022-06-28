import csv
req_file ="C:\\Users\\KARTHIK\\Desktop\\info\\demo.csv"
fo=open(req_file,'w', newline="")
content_writer =csv.writer(fo)
content_writer.writerow(['s_no' , 'name' , 'age'])
content_writer.writerow([1, 'Ram' , 25])
content_writer.writerow([2, 'John' , 24])
fo.close()
