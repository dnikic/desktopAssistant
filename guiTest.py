from tkinter import *
import time
import threading
import webbrowser
import desktopAssistant

threadkiller=True
asistantInstance=desktopAssistant

def loopFunction():
    global asistantInstance
    asistantInstance.lastCommand='No previous command'
    asistantInstance.guiStopApp=False
    asistantInstance.main()
#    print('loopFunction finished')

#    print('Entered loop function')
#    global threadkiller
#    while  threadkiller==True:
#        print ("Looping")
#        time.sleep(1)
#        print('in loop thredkiler is_' +str(threadkiller))
#    print('loopFunction finished')
          

def stopping():
    global asistantInstance
#    global threadkiller
#    print('Stopping')
#    threadkiller=False
    asistantInstance.guiStopApp=True
#    asistantInstance.lastCommand='assistant exit'
#    print(asistantInstance.lastCommand)  
    

def startThread1():
    t = threading.Thread(target = loopFunction, name = 'thread1', args =() )
    t.start()


def quitapp():
#    asistantInstance.guiStopApp=True
    master.destroy()

def helpPage():
    url = 'https://github.com/dnikic/desktopAssistant/blob/master/README.md'
    webbrowser.open(url)

def unstop():
    global threadkiller
    threadkiller=True
    print('Unstopping')
    print(threadkiller)



master = Tk()
b = Button(master, text="Assistant On", command=startThread1)
b.pack()
b2 = Button(master, text="Assistant off", command=stopping)
b2.pack()
#b3 = Button(master, text="UnStop", command=unstop)
#b3.pack()
b4 = Button(master, text="Help", command=helpPage)
b4.pack()
b5 = Button(master, text="Quit", command=quitapp)
b5.pack()
 
mainloop()
