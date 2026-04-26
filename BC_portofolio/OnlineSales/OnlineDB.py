import sqlite3 as sq3
import pandas as pd

#CREATING SQLITE CONNECTION

def create_Sqlite_connection(loc_path, db_name):
    conn = loc_path + db_name
    connection = sq3.connect(conn)
    print("Database created.")
    return connection

def create_tables(conn):
    cur = conn.cursor()

    #CUSTOMER TABLE
    cur.execute('''
         CREATE TABLE IF NOT EXISTS customers(
            CustomerID INT PRIMARY KEY,
            Country TEXT
        );
    ''')
    #PRODUCTS TABLE
    cur.execute('''
         CREATE TABLE IF NOT EXISTS products(
             Stockcode TEXT PRIMARY KEY,
             Description TEXT,
             UnitPrice INT
        );
    ''')
    #TRANSACTIONS TABLE
    cur.execute('''
         CREATE TABLE IF NOT EXISTS transactions (
              InvoiceNo TEXT,
              CustomerID INT,
              StockCode TEXT,
              Quantity INT,
              InvoiceDate TEXT,
              UnitPrice REAL,
              TotalAmount_GBP REAL,
              FOREIGN KEY(CustomerID) REFERENCES customers(CustomerID),
              FOREIGN KEY(StockCode) REFERENCES products(StockCode) 
        );
    ''')
    
    #LOADING CSV AND INSERTING DATA         
def readcsv(loc, fname):
    locateFile = loc + fname
    df = pd.read_csv(locateFile) 
    df = df.dropna()
    return df

def writecsv_to_db(df, tableName, conn):
    df.to_sql(tableName, conn, if_exists ='replace', index = False)

    #LOADING CSV
def populate_db(loc, conn):
    cust = readcsv(loc, 'customers.csv')
    prod = readcsv(loc, 'products.csv')
    trans =readcsv(loc,'transactions.csv')

    #WRITING DATA  TO TABLES
    writecsv_to_db(cust, 'customers', conn)
    writecsv_to_db(prod, 'products', conn)
    writecsv_to_db(trans, 'transactions', conn)