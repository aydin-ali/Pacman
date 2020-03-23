def setup():
    global minim, intro, gameMusic, gameOverMusic, eatingMusic
    #Sound and Music variables
    add_library ('minim')
    minim = Minim(this)
    intro = minim.loadFile("PacmanTheme.mp3")
    gameMusic = minim.loadFile("PacmanGameMusic.mp3")
    gameOverMusic = minim.loadFile("GameOver.mp3")
    size(800, 800)
    background(0, 0, 0)
    startup()

def startup():
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth
    global pmanx, pmany, pmanw, pmanh, pman, pman2, pman3, pman4, showpman, incrPmanX, incrPmanY
    global ghost, numghosts, ghostinfo, allghostinfo
    global inky, pinky, blinky, clyde
    global numdots, dotinfo, alldotinfo
    global whichKey, goLeft, goRight, goUp, goDown, characterSet
    global upperBound, bottomBound, leftBound, rightBound
    global gamemode
    global score
    global arrowcontrols, pkey, ghost, dots, backarrow
    global startRectX, startRectY, rectXShow, rectYShow, rectHeight, rectWidth
    global startRectX2, startRectY2, rectXShow2, rectYShow2, rectHeight2, rectWidth2

    mode = 0    
# Menu variables
    back = loadImage("pacman.png")
    imageheight = 640
    imagewidth = 360
    imageCornerPointX = 80
    imageCornerPointY = 220
    font = createFont("Phosphate", 16, True)
    numSquares = 3
    startSquareX = 125
    startSquareY = 550
    squareHeight = 150
    squareWidth = 150
# Game screen variables
    pmanx = 56
    pmany = 56
    pmanw = 25
    pmanh = 25
    incrPmanX = 5
    incrPmanY = 5
    pman = loadImage("pman.png")
    pman2 = loadImage("pman2.png")
    pman3 = loadImage("pman3.png")
    pman4 = loadImage("pman4.png")
    showpman = pman
    whichKey = ""
    characterSet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ0"]
    goLeft = "A"
    goRight = "S"
    goUp = "W"
    goDown = "D"
    leftBound = 55
    rightBound = 745
    upperBound = 55
    bottomBound = 745
    ghost = loadImage("ghost.png")
    inky = loadImage("inky.png")
    pinky = loadImage("pinky.png")
    blinky = loadImage("blinky.png")
    clyde = loadImage("clyde.png")
    numghosts = 4
    ghostx = 0
    ghosty = 0
    ghostw = 0
    ghosth = 0
    incrGhostX = 0
    incrGhostY = 0
    ghostinfo = [ghost, ghostx, ghosty, ghostw, ghosth, incrGhostX, incrGhostY]
    allghostinfo = [ghostinfo[:] for i in range(numghosts)]
    allghostinfo[0] = [inky, 375, 275, 25, 25, 2, 2]
    allghostinfo[1] = [pinky, 600, 575, 25, 25, 2, 2]
    allghostinfo[2] = [blinky, 175, 400, 25, 25, 2, 2]
    allghostinfo[3] = [clyde, 250, 650, 25, 25, 2, 2]
    numdots = 40
    dotx = 0
    doty = 0
    dotw = 0
    doth = 0
    dotinfo = [dotx, doty, dotw, doth]
    alldotinfo = [dotinfo[:] for i in range(numdots)]
    alldotinfo[0] = [200, 80, 10, 10]
    alldotinfo[1] = [300, 80, 10, 10]
    alldotinfo[2] = [400, 80, 10, 10]
    alldotinfo[3] = [500, 80, 10, 10]
    alldotinfo[4] = [600, 80, 10, 10]
    alldotinfo[5] = [200, 200, 10, 10]
    alldotinfo[6] = [300, 200, 10, 10]
    alldotinfo[7] = [400, 200, 10, 10]
    alldotinfo[8] = [500, 200, 10, 10]
    alldotinfo[9] = [600, 200, 10, 10]
    alldotinfo[10] = [200, 300, 10, 10]
    alldotinfo[11] = [300, 300, 10, 10]
    alldotinfo[12] = [400, 300, 10, 10]
    alldotinfo[13] = [500, 300, 10, 10]
    alldotinfo[14] = [600, 300, 10, 10]
    alldotinfo[15] = [200, 515, 10, 10]
    alldotinfo[16] = [300, 515, 10, 10]
    alldotinfo[17] = [400, 515, 10, 10]
    alldotinfo[18] = [500, 515, 10, 10]
    alldotinfo[19] = [600, 515, 10, 10]
    alldotinfo[20] = [200, 600, 10, 10]
    alldotinfo[21] = [300, 600, 10, 10]
    alldotinfo[22] = [400, 600, 10, 10]
    alldotinfo[23] = [500, 600, 10, 10]
    alldotinfo[24] = [600, 600, 10, 10]
    alldotinfo[25] = [200, 720, 10, 10]
    alldotinfo[26] = [300, 720, 10, 10]
    alldotinfo[27] = [400, 720, 10, 10]
    alldotinfo[28] = [500, 720, 10, 10]
    alldotinfo[29] = [600, 720, 10, 10]
    alldotinfo[30] = [100, 200, 10, 10]
    alldotinfo[31] = [100, 300, 10, 10]
    alldotinfo[32] = [700, 200, 10, 10]
    alldotinfo[33] = [700, 300, 10, 10]
    alldotinfo[34] = [100, 515, 10, 10]
    alldotinfo[35] = [100, 600, 10, 10]
    alldotinfo[36] = [700, 515, 10, 10]
    alldotinfo[37] = [700, 600, 10, 10]
    alldotinfo[38] = [200, 408, 10, 10]
    alldotinfo[39] = [600, 408, 10, 10]
    gamemode = 1
    score = 0
# Help screen variables
    arrowcontrols = loadImage("arrowcontrols.png")
    pkey = loadImage("pkey.png")
    dots = loadImage("dots.png")
    backarrow = loadImage("backarrow.png")
# Paused menu variables
    font = createFont("Phosphate", 16, True)
    startRectX = 250
    startRectY = 225
    rectXShow = startRectX
    rectYShow = startRectY
    rectHeight = 100
    rectWidth = 300
# Game over menu variables
    font = createFont("Phosphate", 16, True)
    startRectX2 = 250
    startRectY2 = 325
    rectXShow2 = startRectX2
    rectYShow2 = startRectY2
    rectHeight2 = 100
    rectWidth2 = 300

def draw():
    global minim, intro, gameMusic, gameOverMusic
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth
    global ghost, numghosts, ghostinfo, allghostinfo
    global numdots, dotinfo, alldotinfo
    global pmanx, pmany, pmanw, pmanh, pman
    global gamemode
    global arrowcontrols, escapebutton, ghost, dots

    if mode == 0:
        # gameOverMusic.pause()
        # gameMusic.pause()
        menu()
    elif mode == 1:
        # gameOverMusic.pause()
        intro.pause()
        gamescreen()
    elif mode == 2:
        helpscreen()
    elif mode == 3:
        highscores()
    elif mode == 4:
        paused()
    elif mode == 5:
        helpscreen2()
    elif mode == 6:
        gamemode = 1
        # gameMusic.pause()
        gameover1()
    elif mode == 7:
        gamemode = 1
        # gameMusic.pause()
        gameover2()
    
    if gamemode == 2:
        mode = 6
    if gamemode == 3:
        mode = 7

def mousePressed():
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth
    global ghost, numghosts, ghostinfo, allghostinfo
    global pmanx, pmany, pmanw, pmanh, pman
    global gamemode
    global arrowcontrols, escapebutton, ghost, dots

    if mode == 0:
        if mouseX >= 127 and mouseX <= 276:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                startup()
                mode = 1
        if mouseX >= 327 and mouseX <= 476:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                mode = 2
        if mouseX >= 527 and mouseX <= 676:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                mode = 3

    if mode == 2:
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 0

    if mode == 3:
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 0

    if mode == 4:
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 225 and mouseY <= 325:
                background(0, 0, 0)
                mode = 1
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 425 and mouseY <= 525:
                background(0, 0, 0)
                mode = 5
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 625 and mouseY <= 725:
                background(0, 0, 0)
                mode = 0

    if mode == 5:
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 4
    
    if mode == 6:
        if mouseY >= 325 and mouseY <= 425:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                startup()
                mode = 1
        if mouseY >= 525 and mouseY <= 625:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                mode = 0
    
    if mode == 7:
        if mouseY >= 325 and mouseY <= 425:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                startup()
                mode = 1
        if mouseY >= 525 and mouseY <= 625:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                mode = 0
                
def keyPressed():
    global mode
    global whichKey

    if mode == 1:
        if (keyCode == UP):
            whichKey = "W"
        elif (keyCode == DOWN):
            whichKey = "D"
        elif (keyCode == LEFT):
            whichKey = "A"
        elif (keyCode == RIGHT):
            whichKey = "S"
        if (key == 'P' or key == 'p'):
            background(0, 0, 0)
            mode = 4

def menu():
    global mode
    global minim, intro
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth

    background(0, 0, 0)
    
    intro.play()

    textFont(font, 150)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("P A C M A N", 400, 200)
    image(back, imageCornerPointX, imageCornerPointY, imageheight, imagewidth)

    stroke(0, 0, 0)
    fill(255, 220, 75)
    rect(startSquareX, startSquareY, squareWidth, squareHeight)
    rect(startSquareX + squareWidth + 50,
         startSquareY, squareWidth, squareHeight)
    rect(startSquareX + squareWidth * 2 + 100,
         startSquareY, squareWidth, squareHeight)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("START", 200, 640)
    text("HELP", 400, 640)
    text("HIGH", 600, 620)
    text("SCORE", 600, 660)

    if mouseX >= 127 and mouseX <= 276:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX, startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("START", 200, 640)
    if mouseX >= 327 and mouseX <= 476:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX + squareWidth + 50,
                 startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("HELP", 400, 640)
    if mouseX >= 527 and mouseX <= 676:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX + squareWidth * 2 + 100, startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("HIGH", 600, 620)
            text("SCORE", 600, 660)

def gamescreen():
    global gameMusic, eatingMusic
    global pmanx, pmany, pmanw, pmanh, pman, pman2, pman3, pman4, showpman, incrPmanX, incrPmanY
    global whichKey, goLeft, goRight, goUp, goDown, characterSet, goPaused
    global upperBound, bottomBound, leftBound, rightBound
    global numdots, dotinfo, alldotinfo, dotcounter
    global gamemode
    global score
    global font

    background(0, 0, 0)
    
    # gameMusic.play()

    if whichKey == goLeft:
        pmanx += incrPmanX * -1
        showpman = pman2
    
    elif whichKey == goRight:
        pmanx += incrPmanX
        showpman = pman

    if whichKey == goUp:
        pmany += incrPmanY * -1
        showpman = pman4

    elif whichKey == goDown:
        pmany += incrPmanY
        showpman = pman3

    if pmanx >= rightBound - pmanw:
        pmanx = rightBound - pmanw
    elif pmanx <= leftBound:
        pmanx = leftBound

    if pmany >= bottomBound - pmanh:
        pmany = bottomBound - pmanh
    elif pmany < upperBound:
        pmany = upperBound
        
    for i in range(numghosts):
        image(allghostinfo[i][0], allghostinfo[i][1], allghostinfo[
              i][2], allghostinfo[i][3], allghostinfo[i][4])
        allghostinfo[i][1] += allghostinfo[i][5]
        allghostinfo[i][2] += allghostinfo[i][6]
        if allghostinfo[i][1] >= rightBound - allghostinfo[i][3]:
            allghostinfo[i][5] = allghostinfo[i][5] * -1
        if allghostinfo[i][1] <= leftBound:
            allghostinfo[i][5] = allghostinfo[i][5] * -1
        if allghostinfo[i][2] >= upperBound:
            allghostinfo[i][6] = allghostinfo[i][6] * -1
        if allghostinfo[i][2] <= bottomBound - allghostinfo[i][4]:
            allghostinfo[i][6] = allghostinfo[i][6] * -1
    
    for i in range(numdots):
        stroke(225, 255, 255)
        fill(225, 255, 255)
        ellipseMode(CENTER)
        ellipse(alldotinfo[i][0], alldotinfo[i][1], alldotinfo[i][2], alldotinfo[i][3])
        if alldotinfo[i][0] >= pmanx and alldotinfo[i][0] <= pmanx + pmanw and alldotinfo[i][1] >= pmany and alldotinfo[i][1] <= pmany + pmanh:
            alldotinfo[i][1] = -100
            score = score  + 10
        if alldotinfo[i][0] <= pmanx and alldotinfo[i][0] >= pmanx + pmanw and alldotinfo[i][1] <= pmany and alldotinfo[i][1] >= pmany + pmanh:
            alldotinfo[i][1] = -100
            score = score  + 10
    
    if pmany + pmanh/2 >= allghostinfo[0][2] and pmany + pmanh/2 <= allghostinfo[0][2] + allghostinfo[0][4] and pmanx + pmanw/2 >= allghostinfo[0][1] and pmanx + pmanw/2 <= allghostinfo[0][1] + allghostinfo[0][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[0][5] = 0
        allghostinfo[0][6] = 0
        delay(500)
        gamemode = 2
    if pmany + pmanh/2 <= allghostinfo[0][2] and pmany + pmanh/2 >= allghostinfo[0][2] + allghostinfo[0][4] and pmanx + pmanw/2 <= allghostinfo[0][1] and pmanx + pmanw/2 >= allghostinfo[0][1] + allghostinfo[0][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[0][5] = 0
        allghostinfo[0][6] = 0
        delay(500)
        gamemode = 2
    
    if pmany + pmanh/2 >= allghostinfo[1][2] and pmany + pmanh/2 <= allghostinfo[1][2] + allghostinfo[1][4] and pmanx + pmanw/2 >= allghostinfo[1][1] and pmanx + pmanw/2 <= allghostinfo[1][1] + allghostinfo[1][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[1][5] = 0
        allghostinfo[1][6] = 0
        delay(500)
        gamemode = 2
    if pmany + pmanh/2 <= allghostinfo[1][2] and pmany + pmanh/2 >= allghostinfo[1][2] + allghostinfo[1][4] and pmanx + pmanw/2 <= allghostinfo[1][1] and pmanx + pmanw/2 >= allghostinfo[1][1] + allghostinfo[1][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[1][5] = 0
        allghostinfo[1][6] = 0
        delay(500)
        gamemode = 2
    
    if pmany + pmanh/2 >= allghostinfo[2][2] and pmany + pmanh/2 <= allghostinfo[2][2] + allghostinfo[2][4] and pmanx + pmanw/2 >= allghostinfo[2][1] and pmanx + pmanw/2 <= allghostinfo[2][1] + allghostinfo[2][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[2][5] = 0
        allghostinfo[2][6] = 0
        delay(500)
        gamemode = 2
    if pmany + pmanh/2 <= allghostinfo[2][2] and pmany + pmanh/2 >= allghostinfo[2][2] + allghostinfo[2][4] and pmanx + pmanw/2 <= allghostinfo[2][1] and pmanx + pmanw/2 >= allghostinfo[2][1] + allghostinfo[2][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[2][5] = 0
        allghostinfo[2][6] = 0
        delay(500)
        gamemode = 2
    
    if pmany + pmanh/2 >= allghostinfo[3][2] and pmany + pmanh/2 <= allghostinfo[3][2] + allghostinfo[3][4] and pmanx + pmanw/2 >= allghostinfo[3][1] and pmanx + pmanw/2 <= allghostinfo[3][1] + allghostinfo[3][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[3][5] = 0
        allghostinfo[3][6] = 0
        delay(500)
        gamemode = 2
    if pmany + pmanh/2 <= allghostinfo[3][2] and pmany + pmanh/2 >= allghostinfo[3][2] + allghostinfo[3][4] and pmanx + pmanw/2 <= allghostinfo[3][1] and pmanx + pmanw/2 >= allghostinfo[3][1] + allghostinfo[3][3]:
        incrPmanX = 0
        incrPmanY = 0
        allghostinfo[3][5] = 0
        allghostinfo[3][6] = 0
        delay(500)
        gamemode = 2
    
    if score == 400:
        delay(500)
        gamemode = 3
    
    stroke(0, 0, 255)    
    line(50, 50, 750, 50)
    line(55, 55, 745, 55)
    line(50, 50, 50, 750)
    line(55, 55, 55, 745)
    line(50, 750, 750, 750)
    line(55, 745, 745, 745)
    line(750, 750, 750, 50)
    line(745, 745, 745, 55)
    
    stroke(255, 0, 0)
    line(105, 105, 155, 105);
    line(105, 105, 105, 155);
    line(105, 155, 155, 155);
    line(155, 155, 155, 105)

    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany >= 105 and pmany <= 155:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1
    
    if pmanx >= 105 and pmanx <= 155 and pmany >= 105 and pmany <= 155:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx >= 105 and pmanx <= 155 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1 
    
    stroke(0, 255, 0)
    line(645, 105, 695, 105);
    line(645, 105, 645, 155);
    line(645, 155, 695, 155);
    line(695, 155, 695, 105)
    
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany >= 105 and pmany <= 155:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1
    
    if pmanx >= 645 and pmanx <= 695 and pmany >= 105 and pmany <= 155:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx >= 645 and pmanx <= 695 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1
    
    stroke(0, 0, 255)
    line(105, 695, 155, 695);
    line(105, 695, 105, 645);
    line(105, 645, 155, 645);
    line(155, 645, 155, 695)
    
    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany >= 645 and pmany <= 695:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goDown:
            pmany = 645 - pmanh - 1
    
    if pmanx >= 105 and pmanx <= 155 and pmany >= 645 and pmany <= 695:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx >= 105 and pmanx <= 155 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goDown:
            pmany = 645 - pmanh - 1
    
    stroke(255, 0, 0)
    line(645, 695, 695, 695);
    line(645, 695, 645, 645);
    line(645, 645, 695, 645);
    line(695, 645, 695, 695)
    
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany >= 645 and pmany <= 695:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goDown:
            pmany = 695 - pmanh - 1
    
    if pmanx >= 645 and pmanx <= 695 and pmany >= 645 and pmany <= 695:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx >= 645 and pmanx <= 695 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goDown:
            pmany = 645 - pmanh - 1
    
    stroke(0, 255, 0)
    line(350, 350, 450, 350);
    line(350, 350, 350, 450);
    line(350, 450, 450, 450);
    line(450, 350, 450, 450)
    
    if pmanx + pmanw >= 350 and pmanx + pmanw <= 450 and pmany >= 350 and pmany <= 450:
        if whichKey == goRight:
            pmanx = 350 - pmanw - 1
        if whichKey == goUp:
            pmany = 450 + 1
   
    if pmanx + pmanw >= 350 and pmanx + pmanw <= 450 and pmany + pmanh >= 350 and pmany + pmanh <= 450:
        if whichKey == goRight:
            pmanx = 350 - pmanw - 1
        if whichKey == goDown:
            pmany = 350 - pmanh - 1
    
    if pmanx >= 350 and pmanx <= 450 and pmany >= 350 and pmany <= 450:
        if whichKey == goLeft:
            pmanx = 450 + 1
        if whichKey == goUp:
            pmany = 450 + 1
   
    if pmanx >= 350 and pmanx <= 450 and pmany + pmanh >= 350 and pmany + pmanh <= 450:
        if whichKey == goLeft:
            pmanx = 450 + 1
        if whichKey == goDown:
            pmany = 350 - pmanh - 1
    
    stroke(255, 0, 0)
    line(320, 105, 480, 105);
    line(320, 105, 320, 155);
    line(320, 155, 480, 155);
    line(480, 105, 480, 155)
    
    if pmanx + pmanw >= 320 and pmanx + pmanw <= 480 and pmany >= 105 and pmany <= 155:
        if whichKey == goRight:
            pmanx = 320 - pmanw - 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx + pmanw >= 320 and pmanx + pmanw <= 480 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goRight:
            pmanx = 320 - pmanw - 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1
    
    if pmanx >= 320 and pmanx <= 480 and pmany >= 105 and pmany <= 155:
        if whichKey == goLeft:
            pmanx = 480 + 1
        if whichKey == goUp:
            pmany = 155 + 1
   
    if pmanx >= 320 and pmanx <= 480 and pmany + pmanh >= 105 and pmany + pmanh <= 155:
        if whichKey == goLeft:
            pmanx = 480 + 1
        if whichKey == goDown:
            pmany = 105 - pmanh - 1
    
    stroke(0, 255, 0)
    line(320, 695, 480, 695);
    line(320, 695, 320, 645);
    line(320, 645, 480, 645);
    line(480, 695, 480, 645)
    
    if pmanx + pmanw >= 320 and pmanx + pmanw <= 480 and pmany >= 645 and pmany <= 695:
        if whichKey == goRight:
            pmanx = 320 - pmanw - 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx + pmanw >= 320 and pmanx + pmanw <= 480 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goRight:
            pmanx = 320 - pmanw - 1
        if whichKey == goDown:
            pmany = 645 - pmanh - 1
    
    if pmanx >= 320 and pmanx <= 480 and pmany >= 645 and pmany <= 695:
        if whichKey == goLeft:
            pmanx = 480 + 1
        if whichKey == goUp:
            pmany = 695 + 1
   
    if pmanx >= 320 and pmanx <= 480 and pmany + pmanh >= 645 and pmany + pmanh <= 695:
        if whichKey == goLeft:
            pmanx = 480 + 1
        if whichKey == goDown:
            pmany = 645 - pmanh - 1
    
    stroke(0, 0, 255)
    line(105, 320, 105, 480);
    line(105, 320, 155, 320);
    line(155, 320, 155, 480);
    line(105, 480, 155, 480)
    
    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany >= 320 and pmany <= 480:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goUp:
            pmany = 480 + 1
   
    if pmanx + pmanw >= 105 and pmanx + pmanw <= 155 and pmany + pmanh >= 320 and pmany + pmanh <= 480:
        if whichKey == goRight:
            pmanx = 105 - pmanw - 1
        if whichKey == goDown:
            pmany = 320 - pmanh - 1
    
    if pmanx >= 105 and pmanx <= 155 and pmany >= 320 and pmany <= 480:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goUp:
            pmany = 480 + 1
   
    if pmanx >= 105 and pmanx <= 155 and pmany + pmanh >= 320 and pmany + pmanh <= 480:
        if whichKey == goLeft:
            pmanx = 155 + 1
        if whichKey == goDown:
            pmany = 320 - pmanh - 1
    
    stroke(255, 0, 0)
    line(695, 320, 695, 480);
    line(695, 320, 645, 320);
    line(645, 320, 645, 480);
    line(695, 480, 645, 480)
    
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany >= 320 and pmany <= 480:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goUp:
            pmany = 480 + 1
   
    if pmanx + pmanw >= 645 and pmanx + pmanw <= 695 and pmany + pmanh >= 320 and pmany + pmanh <= 480:
        if whichKey == goRight:
            pmanx = 645 - pmanw - 1
        if whichKey == goDown:
            pmany = 320 - pmanh - 1
    
    if pmanx >= 645 and pmanx <= 695 and pmany >= 320 and pmany <= 480:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goUp:
            pmany = 480 + 1
   
    if pmanx >= 645 and pmanx <= 695 and pmany + pmanh >= 320 and pmany + pmanh <= 480:
        if whichKey == goLeft:
            pmanx = 695 + 1
        if whichKey == goDown:
            pmany = 320 - pmanh - 1
    
    image(showpman, pmanx, pmany, pmanw, pmanh)
    
    font = createFont("Phosphate", 16, True)

    fill(255, 220, 75)
    textFont(font, 25)
    textAlign = (CENTER)
    text("SCORE: " + str(score), 650, 35)

def helpscreen():
    global minim, intro
    global arrowcontrols, escapebutton, ghost, dots, backarrow
    
    background(0, 0, 0)

    font = createFont("Phosphate", 16, True)

    fill(120, 120, 120)
    rect(35, 170, 730, 600)
    fill(255, 255, 255)
    textFont(font, 150)
    textAlign = (CENTER)
    text("HELP", 400, 130)

    fill(0, 0, 0)
    textFont(font, 40)
    text("GAME CONTROLS", 220, 500)
    text("PRESS 'P' TO PAUSE", 575, 500)
    text("AVOID GHOSTS AND EAT DOTS", 400, 750)
    image(arrowcontrols, 80, 220, 260, 240)
    image(pkey, 470, 210, 200, 200)
    image(ghost, 120, 520, 160, 180)
    image(dots, 470, 520, 220, 180)
    image(backarrow, 0, 0, 40, 40)

    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)

def highscores():
    global minim, intro
    global backarrow

    background(0, 0, 0)

    textFont(font, 110)
    fill(255, 220, 75)
    textAlign = (CENTER)
    text("HIGHSCORES", 400, 100)

    stroke(0, 0, 0)
    rect(80, 150, 650, 600)

    textFont(font, 50)
    fill(0, 0, 0)
    text("POINTS", 500, 200)
    text("NAME", 240, 200)
    text("1.", 100, 260)
    text("2.", 100, 340)
    text("3.", 100, 420)
    text("4.", 100, 500)
    text("5.", 100, 580)
    text("6.", 100, 660)
    text("7.", 100, 740)

    image(backarrow, 0, 0, 40, 40)

    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)

def paused():
    global startRectX, startRectY, rectXShow, rectYShow, rectHeight, rectWidth
    global font

    background(0, 0, 0)

    font = createFont("Phosphate", 16, True)
    textFont(font, 100)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("PAUSED", 400, 100)

    stroke(0, 0, 0)
    fill(255, 220, 75)
    rect(rectXShow, rectYShow, rectWidth, rectHeight)
    rect(rectXShow, rectYShow + rectHeight + 100, rectWidth, rectHeight)
    rect(rectXShow, rectYShow + rectHeight * 2 + 200, rectWidth, rectHeight)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("RESUME", 400, 290)
    text("HELP", 400, 490)
    text("MAIN", 400, 670)
    text("MENU", 400, 710)

    if mouseY >= 225 and mouseY <= 325:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow, rectWidth, rectHeight)
            fill(0, 0, 0)
            text("RESUME", 400, 290)
    if mouseY >= 425 and mouseY <= 525:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow + rectHeight + 100,
                 rectWidth, rectHeight)
            fill(0, 0, 0)
            text("HELP", 400, 490)
    if mouseY >= 625 and mouseY <= 725:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow + rectHeight *
                 2 + 200, rectWidth, rectHeight)
            fill(0, 0, 0)
            text("MAIN", 400, 670)
            text("MENU", 400, 710)

def helpscreen2():
    global arrowcontrols, escapebutton, ghost, dots, backarrow

    background(0, 0, 0)

    font = createFont("Phosphate", 16, True)

    stroke(0, 0, 0)
    fill(120, 120, 120)
    rect(35, 170, 730, 600)
    fill(255, 255, 255)
    textFont(font, 150)
    textAlign = (CENTER)
    text("HELP", 400, 130)

    fill(0, 0, 0)
    textFont(font, 40)
    text("GAME CONTROLS", 220, 500)
    text("PRESS 'P' TO PAUSE", 575, 500)
    text("AVOID GHOSTS AND EAT DOTS", 400, 750)
    image(arrowcontrols, 80, 220, 260, 240)
    image(pkey, 470, 210, 200, 200)
    image(ghost, 120, 520, 160, 180)
    image(dots, 470, 520, 220, 180)
    image(backarrow, 0, 0, 40, 40)

    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)
    
def gameover1():
    global gameOverMusic
    global startRectX2, startRectY2, rectXShow2, rectYShow2, rectHeight2, rectWidth2
    global font

    background(0, 0, 0)
    
    # gameOverMusic.play()

    font = createFont("Phosphate", 16, True)
    textFont(font, 100)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("YOU LOST!", 400, 100)
    
    textFont(font, 50)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("YOU SCORED: " + str(score),  400, 200)

    stroke(0, 0, 0)
    fill(255, 220, 75)
    rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
    rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("RESTART", 400, 390)
    text("MAIN", 400, 570)
    text("MENU", 400, 610)

    if mouseY >= 325 and mouseY <= 425:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("RESTART", 400, 390)
    if mouseY >= 525 and mouseY <= 625:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("MAIN", 400, 570)
            text("MENU", 400, 610)

def gameover2():
    global gameOverMusic
    global startRectX2, startRectY2, rectXShow2, rectYShow2, rectHeight2, rectWidth2
    global font

    background(0, 0, 0)
    
    # gameOverMusic.play()

    font = createFont("Phosphate", 16, True)
    textFont(font, 100)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("YOU WON!", 400, 100)
    
    textFont(font, 50)
    textAlign(CENTER)
    fill(255, 220, 75)
    text("YOU SCORED: " + str(score),  400, 200)

    stroke(0, 0, 0)
    fill(255, 220, 75)
    rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
    rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("RESTART", 400, 390)
    text("MAIN", 400, 570)
    text("MENU", 400, 610)

    if mouseY >= 325 and mouseY <= 425:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("RESTART", 400, 390)
    if mouseY >= 525 and mouseY <= 625:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("MAIN", 400, 570)
            text("MENU", 400, 610)
