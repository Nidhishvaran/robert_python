employee = {'nidhish':21}
name = input('enter your name: ')
age = input('enter your age: ')

if age>='18' and age<'60':
    print('you are eligible to join in this job')
    join = input('are yu wish to join in this job?(yes/no)')
    
    if 'yes' in join:
        salary = input('eneter your required salary per month: ')
        if salary<='5800':
            employee[name]=age.format(age)
            print(employee)
            print('yoiu are succesfully joined in this job sir')
        else:
            print('sir try salary below 5800')
            
    else:
        print('ok sir thankhyou')
        
else:
    print('you not eligible to join in this job sir(hence, you are consider as child labour or old aged labour)')