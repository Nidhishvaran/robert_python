import speech_recognition as sr

listener = sr.Recognizer()
class get_command():
    def get_command():
        try:
            with sr.Microphone() as source:
                print('Listening....................')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
        except Exception as e:
            print(e)
            command = 'nothing'
            
        return command