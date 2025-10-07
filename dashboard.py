# ======================
# Streamlit Sales Dashboard
# ======================

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/sales.csv", encoding='latin1')
data = data.dropna()
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.month
data['Year'] = data['Order Date'].dt.year

# Title
st.title("📊 Sales Data Analysis Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filters")
year = st.sidebar.selectbox("Select Year", sorted(data['Year'].unique()))
region = st.sidebar.selectbox("Select Region", ['All'] + list(data['Region'].unique()))

# Filter data
filtered_data = data[data['Year'] == year]
if region != 'All':
    filtered_data = filtered_data[filtered_data['Region'] == region]

st.write(f"### Showing data for {year}, Region: {region}")
st.dataframe(filtered_data.head())

# Monthly sales trend
st.subheader("📈 Monthly Revenue Trend")
monthly_sales = filtered_data.groupby('Month')['Sales'].sum()
fig1, ax1 = plt.subplots()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', ax=ax1)
st.pyplot(fig1)

# Top 5 products
st.subheader("🏆 Top 5 Best-Selling Products")
top_products = filtered_data.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(5)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis", ax=ax2)
st.pyplot(fig2)

# Profit by category
st.subheader("💰 Profit by Product Category")
fig3, ax3 = plt.subplots()
sns.barplot(x='Category', y='Profit', data=filtered_data, estimator=sum, ci=None, palette="mako", ax=ax3)
st.pyplot(fig3)
