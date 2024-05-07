import mysql.connector

# Dictionary which stores all of the credentials needed to access the SQL Database.
configuration = {
  "user": "root",
  "password": "",
  "host": "127.0.0.1",
  "port": "3306",
  "database": "crook_log_leisure_centre_db"
}

# Attempts to connect to the Database backend via Python.
try:
  connection = mysql.connector.connect(**configuration)
  cursor = connection.cursor(buffered=True)

# If the connection cannot be established, then the print statements below are executed.
except:
  print("XAMPP Server is Not Running.")
  quit()

