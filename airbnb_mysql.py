import mysql.connector

query1 = 'CREATE DATABASE IF NOT EXISTS airbnb;'
query = 'CREATE TABLE IF NOT EXISTS apartment'
query += ' ('
query += '        id INTEGER AUTO_INCREMENT,'
query += '        neighboourhood VARCHAR(255),'
query += '        latitude DOUBLE,'
query += '        longetude DOUBLE,'
query += '        room_type   VARCHAR(255),'
query += '        price      DOUBLE,'
query += '        number_of_reviews    INTEGER,'
query += '        reviews_per_month    DOUBLE,'
query += '        PRIMARY KEY (id))'

port ='8889'
cnx = mysql.connector.connect(user='root', password='root', host='localhost', port=port)
mycursor = cnx.cursor()
mycursor.execute(query1)
cnx.database = 'airbnb'
mycursor.execute(query)
cnx.close()
