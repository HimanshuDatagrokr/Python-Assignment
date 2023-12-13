from mysql.connector import connect, Error


def fetch_data_generator():
    try:
        conn = connect(
            user='root',
            password='himanshu',
            host='localhost',
            database='datagrokr'
        )

        sql_select_Query = "select * from user_details"
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)

        while True:
            # Fetch one row at a time
            row = cursor.fetchone()

            if not row:
                break

            yield row

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if conn.is_connected():
            conn.close()
            cursor.close()
            print("MySQL connection is closed")

# Using the generator in a loop
for row in fetch_data_generator():
    print("Id =", row[0])
    print("Name =", row[1])
    print("Price =", row[2])
    print("Purchase date =", row[3], "\n")
