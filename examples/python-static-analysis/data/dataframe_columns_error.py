import pandas as pd

df = pd.read_csv("./assets/demo.csv")

# Error: DataFrame `df` has no column named 'demo'
print(df["demo"][0])
