import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Acquisition and Understanding
file_path = 'sample-300-rows.csv'
sales_df = pd.read_csv(file_path)

# Inspect dataset information and glimpse of data
print(sales_df.info())
print(sales_df.head())

# 2. Data Cleaning and Preprocessing
# Convert Order Date and Ship Date to datetime format
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'], errors='coerce')
sales_df['Ship Date'] = pd.to_datetime(sales_df['Ship Date'], errors='coerce')

# Check for missing values per column
print(sales_df.isnull().sum())

# Example: Fill missing Postal Codes with 'Unknown' if any
sales_df['Postal Code'] = sales_df['Postal Code'].fillna('Unknown')

# Create new column for the number of days between Order and Ship dates
sales_df['Order_to_Ship_Duration'] = (sales_df['Ship Date'] - sales_df['Order Date']).dt.days

# 3. Exploratory Data Analysis (EDA)

# Summary statistics for numerical columns
print(sales_df.describe())

# Sales distribution plot
filtered_sales = sales_df[
    (sales_df['Sales'] >= 0) & (sales_df['Sales'] <= 2000)
]['Sales']

plt.figure(figsize=(8, 5))
sns.histplot(
    filtered_sales,
    bins=50,
    kde=True
)
plt.title('Sales Distribution (Excluding Outliers)')
plt.xlabel('Sales')
plt.ylabel('Count')
plt.xlim(0, 2000)  # Adjust this range as needed for your data
plt.show()


# Profit distribution plot
plt.figure(figsize=(8, 5))
sns.histplot(sales_df[(sales_df['Profit'] >= -500) & (sales_df['Profit'] <= 500)]['Profit'], bins=50, kde=True, color='green')
plt.title('Profit Distribution (Excluding Outliers)')
plt.xlabel('Profit')
plt.ylabel('Count')
plt.xlim(-500, 500)  # Focus on the central range for readability
plt.show()


# Total Sales by Category bar plot
plt.figure(figsize=(10,6))
category_sales = sales_df.groupby('Category')['Sales'].sum().reset_index()
sns.barplot(data=category_sales, x='Category', y='Sales')
plt.title('Total Sales by Category')
plt.show()

# Total Profit by Region bar plot
plt.figure(figsize=(10,6))
region_profit = sales_df.groupby('Region')['Profit'].sum().reset_index()
sns.barplot(data=region_profit, x='Region', y='Profit')
plt.title('Total Profit by Region')
plt.show()

# Sales trend over time (monthly)
sales_df.set_index('Order Date', inplace=True)
monthly_sales = sales_df['Sales'].resample('M').sum()

plt.figure(figsize=(12,6))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Date')
plt.show()
