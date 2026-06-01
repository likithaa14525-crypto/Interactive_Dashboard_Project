import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("data.csv")

st.title("📊 Interactive Dashboard")

# Sidebar filter
region = st.sidebar.selectbox("Select Region", data["Region"].unique())

filtered_data = data[data["Region"] == region]

# KPI Metrics
st.subheader("Key Metrics")
st.write(filtered_data.describe())

# Bar Chart
st.subheader("Sales by Category")
fig1 = px.bar(filtered_data, x="Category", y="Sales", color="Category")
st.plotly_chart(fig1)

# Line Chart
st.subheader("Trend Analysis")
fig2 = px.line(filtered_data, x="Date", y="Sales")
st.plotly_chart(fig2)

# Pie Chart
st.subheader("Profit Distribution")
fig3 = px.pie(filtered_data, names="Category", values="Profit")
st.plotly_chart(fig3)
st.metric("Total Sales", filtered_data["Sales"].sum())
st.metric("Total Profit", filtered_data["Profit"].sum())
st.title("📊 Sales Interactive Dashboard")
st.subheader("Analyze Region-wise Performance")
date = st.sidebar.selectbox("Select Date", data["Date"].unique())
filtered_data = data[data["Date"] == date]