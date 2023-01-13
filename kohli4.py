import pandas as pd

df =pd.read_csv("Virat_Kohli.csv")
print(df)

#print(df.head(10))

#print(df.tail(10))

#df.info()
#print(df.shape)
#print(df["Opposition"].describe)

#run_frequency = df["Opposition"].value_counts
#print(run_frequency)


#new_df  = df[["runs", "SR", "Opposition"]]
#print(new_df)


vs_aus = df[df["Opposition"]== "v Australia"]
print(vs_aus)

