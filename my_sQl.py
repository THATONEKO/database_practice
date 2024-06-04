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

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")"""


# inserting data in the mysql database

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# required to make changes
mydb.commit()

print(mycursor.rowcount, "record inserted.")"""

# inserting multi number data in the database

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val =[
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

# required for many rows
mycursor.executemany(sql, val)

mydb.commit()

# printing row number 
print(mycursor.rowcount, "was inserted.")

# printing last row id  
print("1 record inserted, ID:", mycursor.lastrowid)"""

# selecting from the table in my database

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# retrieving all the data using the fetch all method 
myresult = mycursor.fetchall()

# printing every row
for x in myresult:
  print(x)"""

# fetching just one row of data from the database

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# retrieving one row of the database using the fetchone method 
myresult = mycursor.fetchone()

print(myresult)"""

# selecting data with filter

"""import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="newpassword",
  database="myapp"
  )

mycursor = mydb.cursor()

# filtering data with address 
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

# retrieving all the data in terms of the filter
myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""

# retrieving records which contains the same phrase

"""import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="newuser",
 password="newpassword",
 database="myapp"
)

mycursor = mydb.cursor()

# filter records with LIKE then the common phrase in the address
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""


# preventing sql injections
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)"""

# sorting records by alphabetical order
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)"""

# descending order of records
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)"""

# deleting specified records
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

# using DELETE  and WHERE
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) delete")"""

# preventing sql injection when deleting

"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) delete")"""

# deleting the whole table
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)"""

# method for deleting a table with condition that it exists or not
"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    password="newpassword",
    database="myapp"
)

mycursor = mydb.cursor()

# IF EXISTS METHOD to check the existence of the table
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)"""

