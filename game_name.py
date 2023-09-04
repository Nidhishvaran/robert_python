import subprocess
while True:
                    game = input("Enter the name of the game you want to play: ")
                    try:
                                        subprocess.call(game+".py", shell=True) 
                                        break
                    except:
                                        print("please enter the valid game name!")