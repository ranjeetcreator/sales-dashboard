import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")
df = pd.read_csv("cleaned_sales.csv")

st.title("Sales Data Dashboard")

regions = sorted(df["Region"].unique())
cats = sorted(df["Category"].unique())
years = sorted(df["Year"].unique())

region = st.sidebar.multiselect("Region", regions, default=regions)
cat = st.sidebar.multiselect("Category", cats, default=cats)
year = st.sidebar.multiselect("Year", years, default=years)

f = df[df["Region"].isin(region) & df["Category"].isin(cat) & df["Year"].isin(year)]

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"${f['Sales'].sum():,.0f}")
c2.metric("Total Orders", f["Order ID"].nunique())
c3.metric("Avg Order Value", f"${f['Sales'].sum() / max(f['Order ID'].nunique(), 1):,.0f}")

left, right = st.columns(2)

cat_sales = f.groupby("Category")["Sales"].sum().reset_index()
left.plotly_chart(px.bar(cat_sales, x="Category", y="Sales", title="Sales by Category"), use_container_width=True)

reg_sales = f.groupby("Region")["Sales"].sum().reset_index()
right.plotly_chart(px.pie(reg_sales, names="Region", values="Sales", title="Sales by Region"), use_container_width=True)

m = f.groupby(["Year", "Month"])["Sales"].sum().reset_index()
m["Date"] = pd.to_datetime(dict(year=m["Year"], month=m["Month"], day=1))
st.plotly_chart(px.line(m, x="Date", y="Sales", title="Monthly Sales Trend"), use_container_width=True)

top = f.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
fig = px.bar(top, x="Sales", y="Product Name", orientation="h", title="Top 10 Products")
fig.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)