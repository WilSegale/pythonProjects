import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Cmonster2006",
  database=""
)

mycursor = mydb.cursor()

# Create a table
mycursor.execute("CREATE TABLE IF NOT EXISTS info (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Insert data into the table
sql = "INSERT INTO your_table (name, age) VALUES (%s, %s)"
val = ("John", 30)
mycursor.execute(sql, val)
mydb.commit()

# Fetch data from the table
mycursor.execute("SELECT * FROM your_table")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.close()
