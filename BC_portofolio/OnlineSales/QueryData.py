import sqlite3 as sq3
import pandas as pd

def displaydbtable(queryString,conn):
    dataFrame = pd.read_sql(queryString, conn)
    return dataFrame

#TOTAL QUANTITY SOLD FOR EACH PRODUCT MONTHLY
def quantity_sold_monthly(conn):
    query = '''
    SELECT StockCode, STRFTIME('%m-%Y', InvoiceDate) AS Month, SUM(Quantity) AS Total_Quantity
    FROM transactions
    GROUP BY STRFTIME('%m-%Y', InvoiceDate), StockCode;
    '''
    return displaydbtable(query, conn)

#SALES TRENDS FOR EACH PRODUCT
def sales_trends_each_product(conn):
    query = '''
    SELECT StockCode, STRFTIME('%m-%Y' ,InvoiceDate) AS Month, SUM(TotalAmount_GBP) AS Monthly_sales
    FROM transactions
    GROUP BY STRFTIME('%m-%Y' ,InvoiceDate), StockCode;
    '''
    return displaydbtable(query, conn)

#TOP 5 CUSTOMERS BY TOTAL SALES
def top_5_by_sales(conn):
    query = '''
    SELECT CustomerID, SUM(TotalAmount_GBP) AS Total_sales
    FROM transactions
    GROUP BY CustomerID
    ORDER BY SUM(TotalAmount_GBP) DESC
    LIMIT 5;
    '''
    return displaydbtable(query, conn)

#REVENUE CONTRIBUTION FROM EACH PRODUCT
def revenue_by_each_product(conn):
    query = '''
    SELECT StockCode, SUM(TotalAmount_GBP) AS Revenue_Per_Product
    FROM transactions
    GROUP BY StockCode
    ORDER BY Revenue_Per_Product DESC
    '''
    return displaydbtable(query, conn)