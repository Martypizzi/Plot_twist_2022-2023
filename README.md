```
________  ___       ________  _________        _________  ___       __   ___  ________  _________   
|\   __  \|\  \     |\   __  \|\___   ___\     |\___   ___\\  \     |\  \|\  \|\   ____\|\___   ___\ 
\ \  \|\  \ \  \    \ \  \|\  \|___ \  \_|     \|___ \  \_\ \  \    \ \  \ \  \ \  \___|\|___ \  \_| 
 \ \   ____\ \  \    \ \  \\\  \   \ \  \           \ \  \ \ \  \  __\ \  \ \  \ \_____  \   \ \  \  
  \ \  \___|\ \  \____\ \  \\\  \   \ \  \           \ \  \ \ \  \|\__\_\  \ \  \|____|\  \   \ \  \ 
   \ \__\    \ \_______\ \_______\   \ \__\           \ \__\ \ \____________\ \__\____\_\  \   \ \__\
    \|__|     \|_______|\|_______|    \|__|            \|__|  \|____________|\|__|\_________\   \|__|
                                                                                 \|_________|
```

A Processing (4.0.1) text editor! :speaking_head: :computer: :page_facing_up: :paperclip: :memo: :grey_question:



## Usage

Plot twist is a work that explores the possibilities of the improbable: 

`What would happen if our devices stopped functioning in the way we are used to?`

The subversion of the interface answers this question by inviting us to discover the new functionalities of the device, following the rules that feed its new
functioning.


## How does it work? 

First of all, the code sets several variables such as like the `letterArr` array, which will store all the letter values, the `textArr`, which will then store the written text, the cursor selection `currSell` and the variables to space characters  `xAdd` and  `yAdd`. The last variabile which is set is the `fontSize`.

```python
letterArr=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "?", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
textArr=[]
currSel=0;
yAdd=0
xAdd=0
fontSize=30

The code first runs into the `setup` function by creating a full-screan canvas, a custom mouse cursor

```python
def setup():
    #size(800,800)
    fullScreen(2)
    
    # Mouse cursor
    global posx, posy, puntatore
    posx=0
    posy=0
    puntatore=loadImage("Puntatore.png")
    
    # Set globals for the save button
    global buttonRadius, cancelButtonX, cancelButtonY, textButtonX, textButtonY, posx, posy, cancel, puntatore
    posx, posy=0, 0
    buttonRadius=100
    cancelButtonX, cancelButtonY= width-150, 50
    #textButtonX, textButtonY=width-150, 50
    cancel=loadImage("Print_and_cancel.png")
```



The code implements an inverted mouse and keyboard functionality, where the mouse is used to enter text and the keyboard to navigate with the cursor. The letter is selected by scrolling the mouse, and printed with the right mouse button and deleted with the left mouse button. The cursor position is operated via the keyboard, where keypresses correspond to the direction of the cursor.

