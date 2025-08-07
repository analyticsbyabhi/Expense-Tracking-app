import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',  # Change this
        database='expense_manager'       # Add if needed
    )
    print("Connection successful")
    connection.close()
except mysql.connector.Error as err:
    print("Connection failed:", err)