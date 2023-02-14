# "Plot twist"
# Copyright Martina Pizzigoni, 2022-2023
# The programme was written for the latest version of Processing (4.0.1), and consists of a text editor. 
# The code sets up an interface with a white background, a text window and a delete button. 
# The code implements an inverted mouse and keyboard functionality, where the mouse
# is used to enter text and the keyboard to navigate with the cursor. The letter is then selected 
# by scrolling the mouse, and printed with the right mouse button and deleted with the left. 
# The cursor position is operated via the keyboard, where the key pressure corresponds to the direction of the cursor.


letterArr=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "?", "!", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
textArr=[]
currSel=0;
yAdd=0
xAdd=0
fontSize=30

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
    
    global textArr, letterArr, currSel, xAdd, yAdd, fontSize, posx, posy, saveButtonX, saveButtonY, buttonRadius, gommina
    noCursor()
    
    # Draw the cancel and print button
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
    
    if keyPressed == True:
        loop()
        
    # Display current letter
    global currentsel
    imageMode(CENTER)
    image(currentsel, width-1450, 50, 200, 50)
    textSize(30)
    text(letterArr[currSel], width-1380, 60) # Show printed letter
    
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
        
def mousePressed():
    global textArr, letterArr, currSel
    if mouseButton == LEFT:
        textArr.append(letterArr[currSel])
    elif mouseButton == RIGHT:
        if len(textArr)>0:
            textArr.remove(textArr[len(textArr)-1])
    else:
        print("lol")
    
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
    
def keyPressed():
    global posx, posy, textArr
    global font1, font2, font3, font4
    if key==ENTER:
        print("enter")
        if dist(posx, posy, cancelButtonX, cancelButtonY) < buttonRadius:
            saveFrame("SANKT_interface_MP_####.jpg")
            textArr=[]
    #DOWN keys
    if keyCode==DOWN:
        posy+=10
    if key == 'g' or key == 'h' or key == 'j' or key == 'x' or key == 'c' or key == 'v' or key == 'b' or key == 'n' or key == 'm' or key == ',' or key == ' ' or key == '.' or key == 'z'  or key == '/':
        posy+=10
    #RIGHT keys
    if keyCode==RIGHT:
        posx+=10
    if key == '[' or key == ']' or key == 'k' or key == 'l' or key == ';'  or key == "'" or key == '#' or key == '/'  or key == '-' or key == '=' or key == '.':
        posx+=10
    if key==BACKSPACE:   
        posx+=10
        posy-=10
        print("space")
    #LEFT keys
    if keyCode==LEFT:
        posx-=10  
    if key == '1' or key == '2' or key == 'q' or key == 'w' or key == 'a'  or key == 's' or key == 'd' or key == 'f' or key == '<' or key == 'z' or key == '`':
        posx-=10
    #UP keys
    if keyCode==UP:
        posy-=10
    if key == '1' or key == '`' or key == 'o' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6'  or key == '7' or key == '8' or key == '9' or key == '0' or key == "ß" or key == '´´' or key == "e" or key == 'r' or key == 't' or key == 'y' or key == 'u' or key == 'i' or key == 'p' or key == '-' or key == '=':
        posy-=10
    


# ----------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    
        
