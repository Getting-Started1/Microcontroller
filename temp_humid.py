import serial
import numpy
import matplotlib.pyplot as plt 
import mysql.connector
from drawnow import *


arduinoData = serial.Serial('com4',9600)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M@!n!90!",
    database="myarduinodatabase"
)
mycursor = mydb.cursor()



# mycursor.execute("CREATE TABLE first_ESP32_data (id int AUTO_INCREMENT PRIMARY KEY, temperature float, humidity float,record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
# mycursor.execute("CREATE TABLE first_ESP32_data (id int AUTO_INCREMENT PRIMARY KEY, temperature float, humidity float,record_date TIMESTAMP default NOW() ON UPDATE NOW())")

# mycursor.execute("SELECT * FROM finalizer_data")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)




# mycursor.execute("SELECT * FROM finalizer_data")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)



# mycursor.execute("CREATE TABLE finalizer_data (id int AUTO_INCREMENT PRIMARY KEY, temperature float, humidity float)")







while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline().decode().strip()
    cleanData = arduinoString.split(",")
    tempValue = cleanData[0]
    humidValue = cleanData[1]
    cleanTemp = tempValue.split(":")
    finalTemp = float(cleanTemp[1])
    cleanHumid = humidValue.split(":")
    finalHumid = float(cleanHumid[1])
    sql="INSERT INTO today_real_analysis (temperature,humidity) VALUES (%s,%s)"
    val=(finalTemp, finalHumid)
    mycursor.execute(sql,val)
    mydb.commit()

    print(finalTemp)
    print(finalHumid)
 









    