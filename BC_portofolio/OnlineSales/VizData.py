import matplotlib.pyplot as plt
import QueryData
import seaborn as sns

# BAR CHART 
def total_quantity_for_product_plot(trans):
    trans.groupby('StockCode')['Total_Quantity'].sum().head(20).plot(kind= 'bar', color = 'red')
    plt.xlabel('StockCode')
    plt.ylabel('Total Quantity')
    plt.title('Total Quantity per product')
    plt.show()

# LINE CHART
# References - 'https://seaborn.pydata.org/generated/seaborn.lineplot.html' and 'https://www.youtube.com/watch?v=OR36conyfTc'
def monthly_sales_trends_plot(trans):
    plt.figure(figsize=(12,6))
    product = trans[trans['StockCode'].isin(trans['StockCode'].value_counts().index[:10])]
    sns.lineplot(data=product, x='Month', y='Monthly_sales', hue='StockCode')
    plt.xlabel('Month')
    plt.ylabel('Monthly Sales')
    plt.title('Monthly Sales Trends')
    plt.show()

#HORIZONTAL BAR CHART
def top_5_by_sales_plot(trans):
    trans.groupby('CustomerID')['Total_sales'].sum().nlargest(5).plot(kind = 'barh', color = 'darkblue')
    plt.xlabel('Total Sales')
    plt.ylabel('CustomerID')
    plt.title('Top 5 customers')
    plt.show()

# PIE CHART
def revenue_by_each_product_plot(trans):
    trans.groupby('StockCode')['Revenue_Per_Product'].sum().head(10).plot(kind= 'pie', figsize=(7, 9),     autopct='%1.1f%%')
    plt.show()