import mysql.connector as mc

db = mc.connect(passwd='123456789',user='root',host='localhost',database='9th_standard')

mycursor = db.cursor()
name = input('Enter your name: ')
age = input('enter your age: ')
tamil = input('Enter your tamil mark: ')
english = input('Enter your english mark:')
mathematics = input('enter your mathematics mark: ')
physics = input('Enter your physics mark: ')
chemistry = input('Enter your chemistry mark: ')
biology = input('Enter your biology mark: ')
social_science = input('Enter your social_science mark: ')

if tamil>='35' and english>='35' and mathematics>='35' and physics>='9' and chemistry>='9' and biology>='9' and social_science>='35':
                    result='pass'
                    
else:
                    result='fail'
total_marks = int(tamil)+int(english)+int(mathematics)+int(physics)+int(chemistry)+int(biology)+int(social_science)
sql = ('insert into Class_9th(name ,result,age,tamil_mark ,english_mark ,mathematics_mark,physics_mark,chemistry_mark ,biology_mark ,social_sience_mark,total_marks) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
val = [(name ,result,age,tamil,english,mathematics,physics,chemistry,biology,social_science,total_marks)]
mycursor.executemany(sql,val)
db.commit()
print('succesfully finished!')