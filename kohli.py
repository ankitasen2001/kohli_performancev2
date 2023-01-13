import pandas as pd

df =pd.read_csv("dataset.csv")
print(df)

#print(df.head(10))

#print(df.tail(10))

#df.info()
#print(df.shape)
print(df["Opposition"].describe)



new_df  = df[["runs", "SR", "Opposition"]]
print(new_df)