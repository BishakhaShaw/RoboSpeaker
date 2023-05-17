import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Bishakha")
    while True:
        speak = wincom.Dispatch("SAPI.SpVoice")
        x = input("Enter what you want me to speak: ")
        if x=="q":
            speak.Speak("okay byeeee friend")
            break
        command = f"{x}"
        speak.Speak(command)


