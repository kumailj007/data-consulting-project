import pandas as pd

data = pd.read_csv("sales_data.csv")
data["revenue"] = data["price"] * data["quantity"]

monthly_revenue = data.groupby(data["order_date"].str[:7])["revenue"].sum()
top_products = data.groupby("product")["revenue"].sum().sort_values(ascending=False)

print("Monthly Revenue:")
print(monthly_revenue)

print("\nTop Products by Revenue:")
print(top_products)
