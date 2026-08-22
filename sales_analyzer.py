import pandas as pd

# 1. Creating a fake dataset of a US-based store's sales in Chennai
data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price_INR': [60000, 45000, 3000, 15000, 2500],
    'Quantity_Sold': [5, 12, 40, 8, 25]
}

# 2. Loading the data into a Pandas DataFrame (Table)
df = pd.DataFrame(data)

# 3. Data Science Task: Calculate Total Revenue for each product
df['Total_Revenue'] = df['Price_INR'] * df['Quantity_Sold']

# 4. Display the updated table
print("--- Our E-Commerce Sales Table ---")
print(df)

# 5. Find the highest-selling product category
revenue_by_category = df.groupby('Category')['Total_Revenue'].sum()
print("\n--- Total Revenue by Category ---")
print(revenue_by_category)
