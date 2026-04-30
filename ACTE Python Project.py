#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("E:/ACTE/Data Analyst MAR 2026/Project/Project 1/pizza_sales.csv")


# In[3]:


df


# In[27]:


df.info()


# In[24]:


df.describe()


# # Finding Total Revenue

# In[25]:


df_total_rev = df['total_price'].sum()
df_total_rev 


# # Finding Total Pizza Sold

# In[26]:


df['quantity'].sum()


# In[17]:


df['order_date'].astype


# In[4]:


df['order_date'] = pd.to_datetime(df['order_date'],format='%d-%m-%Y')


# In[28]:


Month_name = df['order_date'].dt.month_name()
Month_name


# In[29]:


df['order_date'].dt.strftime('%b')


# In[30]:


df.columns


# In[7]:


df['order_id']


# In[31]:


df_unq_ord = df['order_id'].nunique()
df_unq_ord


# # Find Average Order Value

# In[32]:


avg_order_pervalue = df_total_rev/df_unq_ord


# In[33]:


avg_order_pervalue


# In[34]:


817860.05/21350


# # Finding Total Order

# In[14]:


df['order_id'].nunique()


# In[35]:


df['quantity'].sum()


# In[36]:


49574/21350


# # Avg Pizza per order

# In[15]:


avg_pizzas_per_order = round(
    df['quantity'].sum() / df['order_id'].nunique(), 2
)

print(avg_pizzas_per_order)


# # Day Trend for Total Orders

# In[20]:


# df['order_date'] = pd.to_datetime(df['order_date'])

result = (
    df.groupby(df['order_date'].dt.day_name())['order_id']
      .nunique()
      .reset_index(name='total_orders')    
)

print(result)


# # Month Trend for Total Orders

# In[21]:


# Convert to datetime (if not already)
# df['order_date'] = pd.to_datetime(df['order_date'])

# Extract month name and count distinct orders
result = (
    df.groupby(df['order_date'].dt.month_name())['order_id']
      .nunique()
#       .reset_index(name='total_orders')
#       .rename(columns={'order_date': 'order_month'})
)

print(result)


# # % of Sales by Pizza Category

# In[38]:


df.groupby('pizza_category')['total_price'].sum()


# In[39]:


# Total revenue (for percentage calculation)
total_revenue = df['total_price'].sum()

# Group by pizza_category
result = (
    df.groupby('pizza_category')['total_price']
      .sum()
      .reset_index(name='total_revenue')
)

# Calculate percentage
result['PCT'] = round((result['total_revenue'] * 100) / total_revenue, 2)

# Round total_revenue to 2 decimal places
result['total_revenue'] = result['total_revenue'].round(2)

print(result)


# # % of Sales by Pizza Size

# In[23]:


# Total revenue (for percentage calculation)
total_revenue = df['total_price'].sum()

# Group by pizza_category
result = (
    df.groupby('pizza_size')['total_price']
      .sum()
      .reset_index(name='total_revenue')
)

# Calculate percentage
result['PCT'] = round((result['total_revenue'] * 100) / total_revenue, 2)

# Round total_revenue to 2 decimal places
result['total_revenue'] = result['total_revenue'].round(2)

print(result)


# # Top 5 Pizzas by Revenue

# In[69]:


result = (
    df.groupby('pizza_name')['total_price']
      .sum()
      .reset_index(name='Total_Revenue')
      .sort_values(by='Total_Revenue', ascending=False)
      .head(5)
)

print(result)


# In[ ]:




