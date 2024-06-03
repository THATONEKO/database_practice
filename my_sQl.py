"""import mysql.connector

# Create a connection object
mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

# Print a success message
print("Connected to MySQL Server")

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query
mycursor.execute("SELECT value FROM iot_data")

# Get the result
result = mycursor.fetchall()

# Print the result
for row in result:
    print(row)
print()
# Close the cursor and connection
mycursor.close()
mydb.close()"""

# checking for the presence of the database
"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)"""

# creating a table
"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")"""

# creating primary key on an existing table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")