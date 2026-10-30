import pandas as pd

df = pd.read_csv("cleaned_sales.csv")
total = df["Sales"].sum()
print("Total Sales:", round(total, 2))

cat = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:\n", cat)
print("\nCategory share %:\n", (cat / total * 100).round(1))

region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:\n", region)

yearly = df.groupby("Year")["Sales"].sum()
print("\nYearly Sales:\n", yearly)

monthly = df.groupby("Month Name")["Sales"].sum().sort_values(ascending=False)
print("\nBest month:", monthly.index[0])

top10 = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top10)