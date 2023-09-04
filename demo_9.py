from mysql.connector import connect

database = connect(host='localhost',
                   user='root',
                   passwd='123456789',
                   database='9th_standard'
                   )

mycursor = database.cursor()
data='use 9th_standard;'
sql='select * from marks_9th'
mycursor.execute(data)
mycursor.execute(sql)

myresult = mycursor.fetchall()
for i in myresult:
    print(i)
database.commit()
print('progress finished without any error!')