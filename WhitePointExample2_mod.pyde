width = 1000
height = 1000
    
def setup():
    global pointX,pointY,pointX_prev, pointY_prev, deltaX, deltaY, it
    size(width,height)
    background(0,0,0)
    pointX = 0
    pointY = 0
    deltaX = 1
    deltaY = 1
    it = 0
    rectMode(CENTER)

    
def draw():
    global pointX, pointY, pointX_prev, pointY_prev, deltaX, deltaY, it
    # translate(width/2,height/2)
    if it == 0:
        pointX_prev = pointX
        pointY_prev = pointY
    pointX += (random(50)-25) * deltaX
    pointY += (random(50)-25) * deltaY
    
    if it%100 == 0:
        global pointX, pointY
        pointX = random(width)
        pointY = random(height)
        noFill()
        stroke(255,0,0)
        strokeWeight(random(2,6))
        
        pushMatrix();
        translate(pointX, pointY)
        rotate(random(PI/2))
        #circle(0, 0, 40 + random(40))
        square(0, 0, 40 + random(40))
        popMatrix()
        
        colCirc = color(255,255,255)
    
    if it%2 == 0:    
        noFill()
        strokeWeight(1)
        stroke(255,255 - map(it%100,0,100,0,255),255 - map(it%100,0,100,0,255))
        circle(pointX, pointY, random(15 ))
    if it != 0 and it%100 != 0:
        line(pointX_prev,pointY_prev,pointX,pointY)
        
    if pointY > height:
        deltaY = -1
    if pointY < 3:
        deltaY = 1
    if pointX > width:
        deltaX = -1
    if pointX < 3:
        deltaX = 1
        
    if keyPressed:
    if key == BACKSPACE:
        global it
        save('result_it' + str(it) + '.jpg')
        exit()
        
    it += 1
    pointX_prev = pointX
    pointY_prev = pointY
        
    
            
    
