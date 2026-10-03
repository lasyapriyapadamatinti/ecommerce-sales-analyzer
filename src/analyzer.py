# DATA ANALYSIS USING PANDAS LIBRARY
import pandas as pd

# Sales data load
df = pd.read_csv("data/sales.csv")

# Calculate the revenue for each sale
df["REVENUE"] = df["QUANTITY"] * df["PRICE"]

# Overall Analysis
total_revenue = df["REVENUE"].sum()
total_units = df["QUANTITY"].sum()
avg_order_value = df["REVENUE"].mean()

# Product analysis
product_sales = df.groupby("PRODUCT")["QUANTITY"].sum()
best_product = product_sales.idxmax()
revenue_by_product = df.groupby("PRODUCT")["REVENUE"].sum()

# Category Analysis
revenue_by_category = df.groupby("CATEGORY")["REVENUE"].sum()
units_by_category = df.groupby("CATEGORY")["QUANTITY"].sum()

# Daily analysis
daily_revenue = df.groupby("DATE")["REVENUE"].sum()

# Display results
print('\n---SALES DATA---')
print(df)

print('\n---OVERALL ANALYSIS---')
print("Total Revenue: ", total_revenue)
print("Total units sold: ", total_units)
print('Average order value: ', avg_order_value)

print('\n---PRODUCT ANALYSIS---')
print('\nUnits sold of product:')
print(product_sales)
print('Best-selling product: ', best_product)
print('Revenue by product: ', revenue_by_product)

print('\n---CATEGORY ANALYSIS---')
print('Revenue by category: ', revenue_by_category)
print('Units sold by category: ', units_by_category)

print('\n---DAILY ANALYSIS---')
print('Daily revenue: ', daily_revenue)

# DATA VISUALIZATION USING MATPLOTLIB LIBRARY
import matplotlib.pyplot as plt

# Category revenue
plt.bar(
    revenue_by_category.index,
    revenue_by_category.values,
    color="#333333"
    )
plt.xlabel(
    'category',
    color="black",
    fontsize = 14)
plt.ylabel(
    'revenue',
    color="black",
    fontsize = 14)
plt.title(
    'REVENUE BY CATEGORY',
    color="black",
    fontweight = "bold",
    fontsize = 14
    )

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.savefig("outputs/revenue_by_category.png")
plt.show()

# Daily revenue
plt.plot(
    daily_revenue.index,
    daily_revenue.values,
    marker='o',
    color="#333333"
    )
plt.xlabel(
    'date',
    color="black",
    fontsize = 14
    )
plt.ylabel(
    'revenue',
    color="black",
    fontsize = 14
    )
plt.title(
    'DAILY REVENUE',
    color="black",
    fontweight = "bold",
    fontsize = 14
    )

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.savefig("outputs/daily_revenue.png")
plt.show()

# Units sold by product
plt.bar(
    product_sales.index,
    product_sales.values,
    color="#333333"
    )
plt.xlabel(
    'product',
    color="black",
    fontsize = 14
    )
plt.ylabel(
    'units sold',
    color="black",
    fontsize = 14
    )
plt.title(
    'UNITS SOLD BY PRODUCT',
    color="black",
    fontweight = "bold",
    fontsize = 14
    )

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.savefig("outputs/units_sold_by_product.png")
plt.show()