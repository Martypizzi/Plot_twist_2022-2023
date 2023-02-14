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

The code implements an inverted mouse and keyboard functionality, where the mouse is used to enter text and the keyboard to navigate with the cursor. The letter is selected by scrolling the mouse, and printed with the right mouse button and deleted with the left mouse button. The cursor position is operated via the keyboard, where keypresses correspond to the direction of the cursor.


## How does it work? 

### Set up of the variables 

First of all, the code sets several variables such as like the `letterArr` array, which will store all the letter values, the `textArr`, which will then store the written text, the cursor selection `currSell` and the variables to space characters  `xAdd` and  `yAdd`. The last variabile which is set is the `fontSize`.

```python
letterArr=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z", "?", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
textArr=[]
currSel=0;
yAdd=0
xAdd=0
fontSize=30
```

### def setup()

The code will first runs into the `setup():` function by creating a full-screan canvas, a custom mouse cursor called `puntatore` and by creating the global variables for the save and delete button.

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

### def draw()

The code then proceeds to create the background, which is drawn in the `draw():` function so it can be refreshed. The background image is loaded, as well as the windows text box.

```python
def draw():
 # Sfondo carosello
    global sfondo, window
    sfondo= loadImage("Sfondo_bianco.jpg")
    imageMode(CORNER)
    image(sfondo, 0, 0, width, height)
    # Text box
    window= loadImage("Windows_window.jpg")
    imageMode(CORNER)
    image(window, 250, 150, width-500, height-250)
```
After that, the global variables are recalled and the cancel and print buttons are also set. In this case, it will be possible to auto-save the page every time the `textArr` is deleted. Each time the cancel button is pressed, the `textArr` will be set back to zero. The button in the upper-left corner which is going to show the current letter selection is also set.

```python
    global textArr, letterArr, currSel, xAdd, yAdd, fontSize, posx, posy, 
    saveButtonX, saveButtonY, buttonRadius, gommina
    noCursor()
    
    global cancel
    ellipseMode(RADIUS)
    strokeWeight(2)
    noStroke()
    noFill()
    circle(cancelButtonX, cancelButtonY, buttonRadius)
    imageMode(CENTER)
    image(cancel, cancelButtonX, cancelButtonY, 200, 50)
    
    # Draw the button wich show the current letter
    global currentsel
    currentsel=loadImage("Current selection.png")
    
    # Draw the button wich show the current letter
    global currentsel
    currentsel=loadImage("Current selection.png")
```
 
The text properties are set, and then the `textArr` is printed: each element of the array is printed individually. The function also includes a conditional statement to check if the text extends beyond the right edge of the screen, in which case it moves down and starts printing on a new line. 

If the length of the text array is greater than the width of the text box, the function saves the current frame as a JPEG image and clears the text array. 

```python
    # Text propeperties
    textAlign(CENTER)
    textSize(fontSize)
    font=loadFont("UnquietSpirits-48.vlw")
    textFont(font)
    
        # Text print
    fill(0)
    if len(textArr)>0:
        for x in range(len(textArr)):
            if 315+xAdd>=width-300:
                yAdd+=70
                xAdd=0
                print(xAdd)
            text(textArr[x],xAdd+315,yAdd+290)
            xAdd+=fontSize/1
        if len(textArr)>362:
            saveFrame("SANKT_interface_MP_####.jpg")
            textArr=[]
    xAdd=0
    yAdd=0
```
The code also includes a section for displaying a current letter, which is stored in an array `currentSel`.

```python
    if keyPressed == True:
        loop()
        
    # Display current letter
    global currentsel
    imageMode(CENTER)
    image(currentsel, width-1450, 50, 200, 50)
    textSize(30)
    text(letterArr[currSel], width-1380, 60) # Show printed letter
``` 

The last part of the `draw()` function aims to draw the custom cursor, controlled by the variables "posx" and "posy". The cursor's position is checked against the boundaries of the screen.

The code also includes a conditional statement that checks if the `ENTER` key has been pressed while the cursor is on the Cancel button in the top right corner of the screen. If the condition is met, the background is refreshed and the `textArr` is cleared.

```python
    # Cursor
    global puntatore
    imageMode(CENTER)
    image(puntatore, posx, posy, 36, 36)
    if keyPressed and (key==ENTER):
        isAtTopRight = (posx >= 460 and posy <= 80)
        background(0)
    if posx<0:
        posx=0
    if posy<0:
        posy=0
    if posx>width-12:
        posx=width-12
    if posy>height-12:
        posy=height-12
```

### def mousePressed()

The `mousePressed()` function is recalled whenever one of these conditions is true:
- `if mouseButton == LEFT` : the selected letter is going to be added to the `textArr` array and therefore printed on screen.
- `elif mouseButton == RIGHT` : the last printed letter is going to be cancelled from the `textArr` array and therefore is going to be cancelled from the screen.

```python
def mousePressed():
    global textArr, letterArr, currSel
    if mouseButton == LEFT:
        textArr.append(letterArr[currSel])
    elif mouseButton == RIGHT:
        if len(textArr)>0:
            textArr.remove(textArr[len(textArr)-1])
```

### def mouseWheel(event)

The `mouseWheel(event)` function selects through the scroll of the mouse wheel the letter to print in the `textArr`. The variable `currSel` picks up the letters from the `letterArr` array, which value cannot be greater than 39 or smaller than zero. This way, the selection cycles through the element of the `currSel` array.

```python
def mouseWheel(event):
    global currSel, letterArr
    if currSel>=0 and currSel<=len(letterArr)-1:
        currSel+=event.getCount()
        currSel= currSel % 39
        if currSel<0:
            currSel=0
        if currSel>len(letterArr)-2:
            currSel=len(letterArr)-1
    print(currSel)
```





