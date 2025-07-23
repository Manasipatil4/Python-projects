import os 


if __name__ == '__main__':
    print("welcome")
    
    while True:
        x = input("enter the text ")
        if x == "q":
            os.system('powershell -Command "Add-Type -AssemblyName System.Speech; '
          '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'byee meet soon\')"')
            break
        command = f'powershell -Command "Add-Type –AssemblyName System.Speech; ' \
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)