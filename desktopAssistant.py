from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import pyautogui
import time


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command,lastCommand):
    "if statements for executing commands"

 

    if 'repeat once' in command:
        command=lastCommand
        print(lastCommand)

#    if 'repeat 5' in command:
#        assistant(lastCommand,lastCommand)
#        assistant(lastCommand,lastCommand)
#        assistant(lastCommand,lastCommand)
#        print('kikiriki')
#        print ('mjau mjau')
#
    elif 'repeat' in command:
        reg_ex = re.search('repeat (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            counter = +int(domain)
            while counter>0:
                assistant(lastCommand,lastCommand)
                counter=counter-1
            lastCommand=command
        else:
            pass

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        lastCommand=command
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
            lastCommand=command
        else:
            pass

    elif 'google' in command:
        reg_ex = re.search('google (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            print('Done!')
            lastCommand=command
        else:
            pass

    elif 'duck' in command:
        reg_ex = re.search('duck (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://duckduckgo.com/?q=' + domain
            webbrowser.open(url)
            lastCommand=command
            print('Done!')
        else:
            pass

    elif 'write' in command:
        reg_ex = re.search('write (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.typewrite(''+domain,0.1)
            print('Written!')
            lastCommand=command
        else:
            pass

    
    elif 'keyboard' in command:
        reg_ex = re.search('keyboard (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.typewrite([''+domain],1)
            print('Pressed!')
            lastCommand=command
        else:
            pass

    elif 'hotkey control alternative shift' in command:
        reg_ex = re.search('hotkey control alternative shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','alt','shift',''+domain)
            print('Ctrl-Alt-Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey ctrl alternative shift' in command:
        reg_ex = re.search('hotkey ctrl alternative shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','alt','shift',''+domain)
            print('Ctrl-Alt-Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass


    elif 'hotkey control alternative' in command:
        reg_ex = re.search('hotkey control alternative (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','alt','shift',''+domain)
            print('Ctrl-Alt hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey ctrl alternative' in command:
        reg_ex = re.search('hotkey ctrl alternative (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','alt',''+domain)
            print('Ctrl-Alt hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass
    
    elif 'hotkey control shift' in command:
        reg_ex = re.search('hotkey control shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','shift',''+domain)
            print('Ctrl-Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey ctrl shift' in command:
        reg_ex = re.search('hotkey ctrl shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl','shift',''+domain)
            print('Ctrl-Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey alternative shift' in command:
        reg_ex = re.search('hotkey alternative shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('alt','shift',''+domain)
            print('Alt-Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass


    elif 'hotkey shift' in command:
        reg_ex = re.search('hotkey shift (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('shift',''+domain)
            print('Shift hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey control' in command:
        reg_ex = re.search('hotkey control (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('ctrl',''+domain)
            print('Ctrl hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass

    elif 'hotkey alternative' in command:
        reg_ex = re.search('hotkey alternative (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            pyautogui.hotkey('alt',''+domain)
            print('Alt hotkey Pressed!'+domain)
            lastCommand=command
        else:
            pass


    elif 'pause toggle' in command:
        pyautogui.typewrite(['space'],1)
        lastCommand=command
        talkToMe('space Pressed!')

    elif 'keyboard next' in command:
        pyautogui.typewrite(['tab'],1)
        lastCommand=command
        talkToMe('tab Pressed!')

    elif 'keyboard previous' in command:
        pyautogui.typewrite(['shift','tab'],1)
        lastCommand=command
        talkToMe('Shift-tab Pressed!')

    elif 'pause youtube' in command:
        pyautogui.typewrite(['k'],1)
        lastCommand=command
        talkToMe('K Pressed!')

    elif 'youtube' in command:
        reg_ex = re.search('youtube (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.youtube.com/results?search_query=' + domain
            webbrowser.open(url)
            lastCommand=command
            print('Done!')
        else:
            pass

    elif 'close window' in command:
        pyautogui.hotkey('alt','f4')
        lastCommand=command
        talkToMe('Alt-F4 Pressed!')


    elif 'what\'s up' in command:
        lastCommand=command
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
            lastCommand=command
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            lastCommand=command
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))
            lastCommand=command

    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')
            lastCommand=command

        else:
            talkToMe('I don\'t know what you mean!')
    return lastCommand


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
lastCommand='No previous command'
while True:
    lastCommand=assistant(myCommand(),lastCommand)







