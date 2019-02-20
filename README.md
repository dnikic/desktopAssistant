# Desktop Assistant
Siri like desktop assistant written in Python which uses google's speech-to-text library to process voice input.

* Install the dependencies in a virtual environment (using conda or virtualenv) to avoid any issues. 

If you are a linux user install the [say](https://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line) command using
```
sudo apt-get install gnustep-gui-runtime
```

```bash
pip2 install -r requirements.txt
pip3 install -r requirements.txt
```

* Usage

```bash
python desktopAssistant.py
````
Or for Gui version:
```bash
python guiTest.py
````


Supported commands :
* Repeat once : Repeats last command
* Repeat : Repeats last command given number of times
* Open reddit subreddit : Opens the subreddit in default browser.
* Open website xyz.com : Opens website at given adress
* Google : Seaches google.com for given word or sentance
* Duck : Seaches duckduckgo.com for given word or sentance
* Wikipedia search : Searches wikipedia.org, returns a list of resalults, and reads the summary of chosen page.
* Write : Writes given text
* Custom script : Executes a external script (Provided by defaul are "First" and "Second" script)
* Window change : Enters Controll+Tab window changing, and expects "select" or "next"
* Keyboard : Simulates a certain keyboard key pressing
* Hotkey control alternative shift : Intiates given key press with hotkey combiantion
* Hotkey control alternative : Intiates given key press with hotkey combiantion
* Hotkey control shift : Intiates given key press with hotkey combiantion
* Hotkey alternative shift : Intiates given key press with hotkey combiantion
* Hotkey shift : Intiates given key press with hotkey combiantion
* Hotkey control : Intiates given key press with hotkey combiantion
* Hotkey alternative : Intiates given key press with hotkey combiantion
* Pause toggle : Simualtes Space keypress as a common video pause hotkey
* Pause youtube : Simualtes k keypress as a youtube.com video pause hotkey
* Keyboard next : Simulates Tab key pressing
* Keyboard previous : Simulates TaShift-b key pressing
* Youtube : searches youtube.com for given video name
* Close window : Simualtes Alt+F4 hotkey pressing
* Assistant stop : Assistand will only listen for Assistant continue command, until revived 
* Assistant exit : Voice assistant will be exited
* Cursor small/medium/large move right/left/sky/down : Moves cursor by a certain amount vertical or horizontal 
* Screen centre : Set cursor at screen center
* Screen origin : Set cursor at top left corner
* Cursor click/double click/triple click : Performs click action
* Cursor right/middle click : Performs right/middle click
* Cursor down/lift : Presses down or lifts left mouse key
* Cursor middle down/lift : Presses down or lifts middle mouse key
* Read copied : Read text copied to clipboard  
* Send email/email : Follow up questions such as recipient name, content will be asked in order.
* Tell a joke/another joke : Says a random dad joke.
* Current weather in {cityname} : Tells you the current condition and temperture
* weather forecast in {cityname} : Tells you the condition, highest and lowest temperture of the next two days
* What's up
