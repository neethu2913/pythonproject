import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="zy"
)

cursor=db.cursor()
sql="insert into employee value(1001,'sruthi','qa',23000)"
cursor.execute(sql)
db.commit()
db.close()