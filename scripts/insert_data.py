import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ecoursemysql",
    database="trading_data"
)

cursor = connection.cursor()

data = pd.read_csv('data/data.csv')

for index, row in data.iterrows():
    sql = "INSERT INTO stock_data (datetime, open, high, low, close, volume, instrument) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (row['datetime'], row['open'], row['high'], row['low'], row['close'], int(row['volume']), row['instrument'])
    cursor.execute(sql, val)

connection.commit()

print(cursor.rowcount, "records inserted.")

cursor.close()
connection.close()
