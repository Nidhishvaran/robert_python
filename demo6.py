from subprocess import call
try:
                    p=call('pip install pyaudio')
                    print(p)
except:
                    print('unable to install this module sir')