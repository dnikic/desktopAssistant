import os

def main():
    #Add code here
    print('Custom Script 1!')
    #opens blender in seporate xfce4-terminal windowfile and runs blenderMacro1.py macro script that enables rotation of light with Ctrl Shift Q hotkey

    os.system("xfce4-terminal -x blender sculptDemo01blend.blend --python blenderMacro1.py")


#if this is uncomented, main() will be executed immidiately on import
#main()

