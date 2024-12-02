import mysql.connector

def get_sql_connection():
  try:
    __cnx = mysql.connector.connect(user='root', password='H@rshit5093', host='localhost', database='grocery_store')  # Update password if necessary
    return __cnx
  except mysql.connector.Error as err:
      print(f"Error: {err}")
      return None