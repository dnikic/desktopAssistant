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
import wikipedia
import pyperclip
import customScript1
import customScript2

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

def windowChanging(command,selected):
    if 'select' in command:
        pyautogui.keyUp('alt')  
        return True
    elif 'next' in command:
        pyautogui.typewrite(['tab'],0.2)
    else:
        return False

def wikipediaChosePage(command, pagesList):
    if command =="wikipedia exit":
        return True 
    else:
        try:
             chosenOption= int(command)
#             print('chosen number is'+ str(chosenOption))
#             print('Daaaayum'+ command)
             print(pagesList[chosenOption])
#             print(wikipedia.page(pagesList[chosenOption]).summary)
             print('\n'+'jobzdon!')
             chosenOutput= str(wikipedia.page(pagesList[chosenOption]).summary)
             chosenOutput=chosenOutput.replace('"','')
             chosenOutput=chosenOutput.replace('(','')
             chosenOutput=chosenOutput.replace(')','')
             chosenOutput=chosenOutput.replace(';','')
#             chosenOutput2=''+chosenOutput
#             print(chosenOutput)    
             talkToMe(chosenOutput)
             return True
        except:
            print('Chosen invalid index number')
            #listen again for index
       
def talkToMeV2 (someString):
    someString=someString.replace('"','')
    someString=someString.replace('(','')
    someString=someString.replace(')','')
    someString=someString.replace(';','')
    talkToMe(someString)

def assistantPause(command):
    if 'assistant continue' in command:
        return True
    else:
        return False


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
            counter=0
            try:
                counter = +int(domain)
            except ValueError:
                pass
            while counter>0:
                assistant(lastCommand,lastCommand)
                counter=counter-1
#            lastCommand=command
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

    elif 'wikipedia search' in command:
        reg_ex = re.search('wikipedia search (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            mylist=wikipedia.search(domain)
#            print(*mylist,sep='\n')
            for number, letter in enumerate(mylist):
#                print(number, letter)
                listOut=str(str(number)+letter )            
                talkToMeV2(listOut)

            
            print('\n'+'Chose number representing page.')
            print('\n'+'Say /wikipedia exit/ to exit selection.')

            while (True):
                if wikipediaChosePage(myCommand(),mylist)==True:
                    break
            print('Wikipedia Done!')
#           lastCommand=command
            
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
    elif 'custom script' in command:
        reg_ex = re.search('custom script (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
#            print(domain)
#            customScript1.main()
            if domain=='first':
                customScript1.main()            
            elif domain=='second':
                customScript2.main()   
            else:
#                print('No such script')                     
                talkToMeV2('No such script')                                     
        else:
            pass

    elif 'window change' in command:
        pyautogui.keyDown('alt')
        time.sleep(3)
#        print('timer over')
        pyautogui.typewrite(['tab'],0.2)
#        time.sleep(3)        
        selected=False
        while selected != True:
            selected=windowChanging(myCommand(),selected)
#            print('in while loop')
        print('Window Changed!')
        lastCommand=command

    
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

    elif 'blender light rotate' in command:
        pyautogui.hotkey('ctrl','shift','q')
        print('Ctrl-Shift-Q hotkey Pressed!')
        lastCommand=command    

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

    elif 'assistant stop' in command:
        talkToMe('Asistant paused')
        while True:
            if assistantPause(myCommand())==True:
                break
        talkToMe('Asistant continued')

    elif 'assistant exit' in command:
        talkToMe('Asistant exiting')
        lastCommand=command


    elif 'cursor small move right' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(maxX/200, 0, duration=0.2)
        lastCommand=command
    elif 'cursor medium move right' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(maxX/50, 0, duration=0.2)
        lastCommand=command
    elif 'cursor large move right' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(maxX/10, 0, duration=0.2)
        lastCommand=command

    elif 'cursor small move left' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(-maxX/200, 0, duration=0.2)
        lastCommand=command
    elif 'cursor medium move left' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(-maxX/50, 0, duration=0.2)
        lastCommand=command
    elif 'cursor large move left' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(-maxX/10, 0, duration=0.2)
        lastCommand=command

    elif 'cursor small move sky' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,-maxY/200, duration=0.2)
        lastCommand=command
    elif 'cursor medium move sky' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,-maxY/50, duration=0.2)
        lastCommand=command
    elif 'cursor large move sky' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,-maxY/10, duration=0.2)
        lastCommand=command
    elif 'cursor small move down' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,maxY/200, duration=0.2)
        lastCommand=command
    elif 'cursor medium move down' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,maxY/50, duration=0.2)
        lastCommand=command
    elif 'cursor large move down' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveRel(0,maxY/10, duration=0.2)
        lastCommand=command

    elif 'screen centre' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveTo(maxX/2, maxY/2)
        lastCommand=command
    elif 'screen origin' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.moveTo(maxX/200, maxY/200)
        lastCommand=command

    elif 'cursor click' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.click(pyautogui.position())
        lastCommand=command
    elif 'cursor double click' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.doubleClick(pyautogui.position())
        lastCommand=command
    elif 'cursor triple click' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.tripleClick(pyautogui.position())
        lastCommand=command
    elif 'cursor right click' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.rightClick(pyautogui.position())
        lastCommand=command
    elif 'cursor middle click' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.middleClick(pyautogui.position())
        lastCommand=command  

    elif 'cursor down' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.mouseDown(pyautogui.position(), button='left')
#        lastCommand=command 
    elif 'cursor lift' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.mouseUp(pyautogui.position(), button='left')
#        lastCommand=command   

    elif 'cursor middle down' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.mouseDown(pyautogui.position(), button='middle')
#        lastCommand=command 
    elif 'cursor middle lift' in command:
        maxX,maxY=pyautogui.size()
        print(maxX,maxY)
        pyautogui.mouseUp(pyautogui.position(), button='middle')
#        lastCommand=command   


    elif 'read copied' in command:
        pasted = pyperclip.paste()
        str(pasted)
        talkToMeV2(pasted)
        lastCommand=command   


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



        else:
            talkToMe('I don\'t know what you mean!')
    return lastCommand

    

talkToMe('I am ready for your command')

#loop to continue executing multiple commands
lastCommand='No previous command'
while True:
    lastCommand=assistant(myCommand(),lastCommand)
    if lastCommand=='assistant exit':
        pyautogui.mouseUp(pyautogui.position(), button='left')
        pyautogui.mouseUp(pyautogui.position(), button='right')
        pyautogui.mouseUp(pyautogui.position(), button='middle')
        break







