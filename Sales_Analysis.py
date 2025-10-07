# ============================
# Sales Data Analysis Dashboard
# ============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load Dataset
data = pd.read_csv("data/sales.csv", encoding='latin1')
print("✅ Dataset Loaded Successfully!")

# 2️⃣ Basic Info
print("\n--- Dataset Info ---")
print(data.info())
print("\n--- First 5 Rows ---")
print(data.head())

# 3️⃣ Handle Missing Values
data = data.dropna()

# 4️⃣ Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# 5️⃣ Extract Month and Year
data['Month'] = data['Order Date'].dt.month
data['Year'] = data['Order Date'].dt.year

# 6️⃣ Monthly Sales Trend
monthly_sales = data.groupby('Month')['Sales'].sum()

plt.figure(figsize=(8,5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# 7️⃣ Top 10 Best-Selling Products
top_products = (
    data.groupby('Product')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

# 8️⃣ Sales by Region
region_sales = data.groupby('Region')['Sales'].sum()

plt.figure(figsize=(7,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# 9️⃣ Profit Analysis
plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Profit', data=data, estimator=sum, ci=None, palette="mako")
plt.title("Total Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

# 🔟 Sales vs Profit Correlation
plt.figure(figsize=(6,5))
sns.scatterplot(x='Sales', y='Profit', data=data, alpha=0.6)
plt.title("Sales vs Profit Correlation")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# 11️⃣ Regional Profit
region_profit = data.groupby('Region')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(7,5))
sns.barplot(x=region_profit.index, y=region_profit.values, palette="Spectral")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()
