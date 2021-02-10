import pymysql

connection = pymysql.connect(host='localhost', port=3300, db='investor', user='root', passwd='1234', autocommit=True)

cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
result = cursor.fetchone()

print ("MariaDB version: {}".format(result[0]))

connection.close()
