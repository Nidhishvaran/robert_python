from mysql.connector import connect

database = connect(host = 'localhost',
                   passwd = '123456789',
                   user='root',
                   database = 'login'
                   )

myc = database.cursor()
myc.execute('select * from signup')
myresult = myc.fetchall()


#l='create table signup(Name varchar(50),UserName varchar(100),password int)'
#l='show tables'
#myc.execute(l)
Name = input('Enter your name: ')
UserName = input('Enter your username: ')
password = input('Enter your password: ')
password = int(password)
sql = 'insert into signup(Name,UserName,password) values(%s,%s,%s)'
val = [(Name,UserName,password)]

myc.executemany(sql,val)


                    
database.commit()
print('your account was created with Name '+Name+' and UserName '+UserName+' your password is ',password)