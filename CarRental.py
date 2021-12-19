import mysql.connector
from mysql.connector import errorcode
# Connecting to the MySQL database
try:
   mydb = mysql.connector.connect(
      user="root",
      password="root",
      host="localhost",
      database="aviano-db")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   
    cursor1 = mydb.cursor()
# Retreive all tables Infomration using the below code
    q1 = ("SELECT * FROM customer") 
    cursor1.execute(q1)
    print("------Customer Table Information--------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")

    q2 = ("SELECT * FROM equipment") 
    cursor1.execute(q2)
    print("------Equipment Table Information------------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    
    q3 = ("SELECT * FROM equipment_type") 
    cursor1.execute(q3)
    print("-----Equipment_type Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q4 = ("SELECT * FROM fuel_option") 
    cursor1.execute(q4)
    print("-----fuel_option Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q5 = ("SELECT * FROM insurance") 
    cursor1.execute(q5)
    print("-----insurance Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q6 = ("SELECT * FROM location") 
    cursor1.execute(q6)
    print("-----location Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q7 = ("SELECT * FROM rental") 
    cursor1.execute(q7)
    print("-----rental Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q8 = ("SELECT * FROM rental_has_equipment_type") 
    cursor1.execute(q8)
    print("-----rental_has_equipment_type Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q9 = ("SELECT * FROM rental_has_insurance") 
    cursor1.execute(q9)
    print("-----rental_has_insurance Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q10 = ("SELECT * FROM rental_invoice") 
    cursor1.execute(q10)
    print("-----rental_invoice Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q11 = ("SELECT * FROM vehicle") 
    cursor1.execute(q11)
    print("----vehicle Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q12 = ("SELECT * FROM vehicle_has_equiment") 
    cursor1.execute(q12)
    print("----vehicle_has_equiment Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")
    q13 = ("SELECT * FROM vehicle_type") 
    cursor1.execute(q13)
    print("----vehicle_type Table Information---------\n")
    for row in cursor1.fetchall():
        
        print(row,"\n")