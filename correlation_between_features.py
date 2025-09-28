import pandas as pd

data = {
  "X" : [1, 2, 3, 4, 5, 6]
  "Y" : [1, 3, 5, 7, 9, 2]
}

df = pd.DataFrame(data)
print(df)

#compare only two features
correlation = df["X"].corr(df["Y"])
print(f"Correlation Calculation is = {correlation}")

#compare all features
correlation = df.corr()
print(f"Correlation Calculation is = {correlation}")
