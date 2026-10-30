import glob
import pandas as pd

path = glob.glob("**/sales.csv", recursive=True)[0]
df = pd.read_csv(path)

df = df.drop_duplicates()
df["Postal Code"] = df["Postal Code"].fillna(0).astype(int)

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%b")

df.to_csv("cleaned_sales.csv", index=False)
print(df.shape)
print(df[["Order Date", "Year", "Month", "Sales"]].head())
print(df.isnull().sum().sum(), "missing values bache")