import mysql.connector
import re
import json
import datetime

def getAllGames(): 
    mydb = mysql.connector.connect(
    host="localhost",
    user="vesperon51",
    passwd="vesperon",
    database = "marcdatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM games")


    data_json = []
    header = [i[0] for i in mycursor.description]
    data = mycursor.fetchall()
    for i in data:
        data_json.append(dict(zip(header, i)))
    print (data_json)
    return data_json