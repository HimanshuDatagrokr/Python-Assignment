from mysql.connector import connect, Error


try:
    conn = connect(
    user = 'root',
    password ='himanshu',
    host = 'localhost',
    database = 'datagrokr')
    
    sql_select_Query = "select * from user_details"
    cursor = conn.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in table:",cursor.rowcount)
    
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0])
        print("Name = ", row[1])
        print("Price = ", row[2])
        print("Purchase date =",row[3],"\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if conn.is_connected():
        conn.close()
        cursor.close()
        print("Mysql connection is closed")
