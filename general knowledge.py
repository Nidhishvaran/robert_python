import pywhatkit
import wikipedia
inp=input('enter you want to know: ')
if inp:
    re=inp.replace('about','')
    try:
        about=wikipedia.summary(re,sentences=2)
        print(about)
    except:
        print('sorry there are no result found')
elif 'about lic' in inp:
    
    print('''
          LIC is known as life insurance corporation
          ''') 
else:
    pass
