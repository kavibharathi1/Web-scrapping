import pandas as pd

df1 = pd.read_json('C:\\Users\\KARTHIK\\Desktop\\json\\file1.json')
print(df1)
df2 = pd.read_json('C:\\Users\\KARTHIK\\Desktop\\json\\file2.json')
print(df2)
df = pd.concat([df1, df2])
print(df)
df.to_csv("CSV.csv", index=False)
result = pd.read_csv("CSV.csv")
print(result)
