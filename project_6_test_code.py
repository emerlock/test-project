import sqlite3
import mysql.connector

# SQL Search
def search_student():
    
    search_user = input('Search for Student:')
    
    mydb = mysql.connector.connect(
      host="192.168.100.134",
      user="admin",
      password=""
    )
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM STUDENTS WHERE name = '" + search_user + "'")

    result = mycursor.fetchone()
    
    return result

def authenticate_login(password):
  if password == "P@SSw0rd!":
    return True
  else:
    return False

print("Welcome to Student Search!")
password = input("Please input password: ")

auth_user = authenticate_login(password)

if auth_user:
  search_student()
else:
  print("Incorrect Password")

