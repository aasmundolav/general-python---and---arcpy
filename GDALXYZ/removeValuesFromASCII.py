import pandas as pd
df = pd.read_csv(r"c:\temp\y.xyz", sep=" ", names=["X","Y","Z"])
print(df.head())               
df = df.query('Z < 10000')
df.to_csv(r"c:\temp\x.xyz", sep=' ', header=None, index=None)
