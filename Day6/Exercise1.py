import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

data = {"Name":["Suman","Ritika","Nijal"],"Age":[21,20,15]}
df = pd.DataFrame(data)
print(df)
print(type(df))

print(df["Name"])

print(df["Age"])

